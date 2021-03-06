.. _much_ado_about_traversal_chapter:

========================
Траверс в Pyramid
========================

.. note:: Это вольный перевод полезной статьи в блоге Роба Миллера (Rob Miller) об альтерантивном URL матчингу способе обработки HTTP запросов в фреймворке Pyramid. Статья также стала частью документации самого фреймворка. Читатель данной статьи должен обладать определенным уровнем знаний и иметь представления о многих аспектах разработки.

Траверс это альтернатива URL диспатчу, принятая в Pyramid.

.. note:: Пользователи знакомые с Zope уже вероятно представляют себе работу алгоритма траверса и могут сразу переходить к главе :ref:`traversal_chapter`, за техническими подробностями. Эта глава нужно в основном людям, работавшим с Pylons, которым сложно понять принцип работы траверса.

Обычно люди, которые долгое время работали с Pylons или с каким-либо другим фреймворком, и с их роутингом URL немного удивляются тому, как устроена обработка и роутинг HTTP запросов в Pyramid и таким понятиям, как траверс и поиск представлений. Другие люди считают, что траверс сложен для понимания. Кто-то думает, что траверс бесполезен, потому как они успешно работали со стандартным URL матчингом и он полностью подходил для их задач. Почему они должны переходить на другой, более сложный, способ роутинга?

Если вы не хотите понимать траверс, то вы можете обойтись без него. Можно без проблем создавать Pyramid приложения и без понимания этой концепции. Тем не менее, в реальной разработке встречается множество задач, которые траверс решает изящнее и лучше, чем классический URL матчинг, основанный на регулярных выражениях. Возможно, вы не сталкивались с такими ситуациями ранее, однако понимание их может помочь вам в будущем. Траверс (traversal) — это, по сути, метафора, легко понятная тем, кто хорошо представляет себе суть директорий и файлов в них.



URL диспатч
------------

Вернемся к классическому роутингу и рассмотрим проблему, которую надо решить. HTTP запрос с адресом передается нашему приложению. Путь запроса повлечет за собой вызов специфичной функции-представления внутри нашего приложения. Мы пытаемся определить, какую функцию-представление (если она существует) мы должны вызвать для текущего URL.

Множество систем, в том числе и Pyramid, предлагают простое решение — обычный URL матчинг. URL матчинг работает так, что парсит URL и сравнивает результаты с множеством явно заданных шаблонов (элементов роутинга), заданных обычными регулярными выражениями (или другим синтаксисом). Каждый такой шаблон (один элемент из множества правил роутера) связан с представлением. Если путь запроса соответствует какому-либо заданному шаблону, то вызывается связанная с ним функция-представление. Если путь запроса подходит сразу нескольким шаблонам, то применяется несколько иная схема разрешения конфликтов, обычно основанная на том, что вызывается та функция-представление, которая совпала с заданным путем запроса раньше и вызывается. Если из всего множества шаблонов, предопределенных разработчиком, не подошел ни один шаблон, то отдается ответ 404 Not Found.

В Pyramid предлагается для использования реализация классического URL матчинга. Используя синтаксис Pyramid мы можем связать шаблон /{userid}/photos/{photoid} с функцией-представлением photo_view(), которая определена в коде. Запрос вида /joeschmoe/photos/photo1 подойдет к этому шаблону и будет вызвана функция photo_view() для обработки запроса. Точно также шаблон /{userid}/blog/{year}/{month}/{postid} может быть привязан к функции blog_post_view() и запрос пути /joeschmoe/blog/2010/12/urlmatching вызовет функцию, которая наверное, знает, как найти и отобразить запрошенный пост блога.

Историческая справка
--------------------

Когда мы немного освежили знания по классическому URL диспетчеру мы можем углубиться в идею траверса. Перед тем, как мы это сделаем давайте немного вспомним историю. Если вы работали некоторое время в веб-разработке, то вы, возможно, помните время, когда не было таких прекрасных фреймворков, как Pylons или Pyramid. Вместо этого, были HTTP серверы общего назначения, которые работали просто как серверы файловой системы. Корень определенного сайта был связан с определенной директорией. Каждый сегмент URL запроса представлял из себя поддиректорию. Последний сегмент пути обычно являлся или директорией или файлом. Когда сервер находил нужный файл, то упаковывал его в HTTP ответ и отправлял обратно клиенту. Таким образом, обслуживание запроса по адресу /joeschmoe/photos/photo1 фактически означало, что на диске должна быть директория joeschmoe, которая в свою очередь содержала директорию с фотографиями, в которой находился файл photo1. Если в процессе обработки пути нужный файл или директория не надились, то отдавался ответ 404 Not Found.

По мере того, как веб становился все более динамичным, добавилась некоторая сложность. Были придуманы технологии: CGI, FastCGI и встраиваемые в веб-сервер модули. Файлы все еще искались в файловой систем, но если имя запрашиваемого файла заканчивалось, например, на .cgi, .pl или .php, или если они были размещены в определенной специальной директории, то в этом случае веб-сервер не отдавал файл в сыром выде, а читал этот файл, исполнял его, используя какой-то интерпретатор, и только потом результат его исполнения отдавал клиенту (HTTP ответ на HTTP запрос). Сервер конфигурировался так, что некоторые файлы вызывали динамический обработчик, а другие файлы просто отдавались в сыром виде веб-сервером (поведение по умолчанию).



Траверс или поиск ресурсов
---------------------------------

.. index::
   single: traversal overview

Верите вы или нет, но если вы понимаете то, как работает отдача файлов из файловой системы, то вы поймете и траверс. И если вы понимаете, что сервер, в зависимости от типа файла, может отдавать разные ответы, то вы поймете и поиск ресурсов.

Основное отличие между поиском в файловой системе и траверсом состоит в том, что файловая система производит поиск во вложенних директориях и файлах, а траверс обходит некоторый объект словарного типа в дереве ресурсов. Рассмотрим пример, чтобы понять, что я имею ввиду:

Путь /joeschmoe/photos/photo1 содержит четыре сегмента: /, joeschmoe, photos и photo1. При поиске в файловой системе у нас была бы корневая директория (/), которая содержит в себе поддиректории (joeschmoe), которая, в свою очередь, содержит другие вложенные директории (photos), а та, в конце концов, содержит JPEG файл (photo1). С траверсом мы имеем корневой объект словарного типа. Поиск по ключу joeschmoe возвращает нам другой словарный объект. Запрашивая вновь у этого объекта по ключу photos, мы получаем другой словарный объект, который в итоге содержит ресурсы, которые мы ищем и значения, которые нам нужны и доступны по ключу photo1.

В понятиях Python траверс или поиск ресуров, который соответствует пути запроса /joeschmoe/photos/photo1 будет выглядеть примерно так:::

    get_root()['joeschmoe']['photos']['photo1']

``get_root()`` — это функция, которая возвращает корневой ресурс траверса. Если все указанные ключи существуют, то возвращаемый ресурс и будет тем ресурсом, который был запрошен, по аналогиии с примером с JPEG файлом, который был бы найден в файловой системе. Если по мере поиска нужного ресурса было создано исключение KeyError, то Pyramid вернет 404 Not Found. (Это не тоже самое, что происходит на самом деле, но основная идея показана верно.)

Что такое ресурс?
---------------------

Вы можете сказать «я понимаю файлы в файловой системе, но что такое эти вложенные словари? Где эти объекты и ресурсы находится? Чем они являются фактически?»

Так как Pyramid не является строгим фреймворком и его целью не является ограничение разработчика, то он и не делает ограничений на то, как ваш ресурс реализован фактически. Разработчик может реализовать ресурс так, как ему угодно. Используется один единственный способ для хранения всех ресурсов (корневой ресурс в том числе), в базе данных в виде графа. Корневой объект — это объект словарного типа. Любой словарный объект в Python реализует метод __getitem__ который вызывается по мере поиска ресурса. Например, если adict является объектом словарного типа, то Python трансформирует вызов типа adict['a'] в adict.__getitem__('a'). Попробуйте это сделать сами, если вы нам не верите:

.. code-block:: text
   :linenos:

   Python 2.4.6 (#2, Apr 29 2010, 00:31:48) 
   [GCC 4.4.3] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>> adict = {}
   >>> adict['a'] = 1
   >>> adict['a']
   1
   >>> adict.__getitem__('a')
   1


Корневой объект словарного типа хранит в себе все идентификаторы его подресурсов как ключи и реализует метод __getitem__, который и отдает их. То есть get_root() отдает уникальный корневой объект, тогда как get_root()['joeschmoe'] отдает объект другого типа, который также хранится в базе данных, который тоже имеет свои собственные подресурсы и реализует метод __getitem__ и так далее вниз по иерархии. Эти ресурсы могут храниться как в реляционной базе данных, так и в одном из популярных сегодня NoSQL хранилищ или где-либо еще. Реального значения это не имеет. До тех пор пока объекты будут представлять API для доступа как к словарю (т.е. будут иметь реализацию метода __getitem__) траверсинг будет работать.

Фактически, вам не нужна база данных. Вы можете использовать обычные простые словари, со структурой вашего сайта, которые буду захардкодены в исходном коде Python. Или вы можете просто реализовать множество объектов с методом __getitem__, который будет искать файлы в нужной директории на диске, и таким образом определить классический традиционный механизм сопоставления пути URL с физическими файлами и директориями в файловой системе через траверс. Другими словами, в этом случае траверс будет являться надмножеством поиска ресурсов в файловой системе.



.. note:: Посмотрите главу :ref:`resources_chapter` для более подробной информации о концепции ресурсов.

Поиск представлений
-----------

Мы почти уже закончили. Мы пояснили весь траверс, который является процессом сопоставления определенного ресурса с заданным специфичным путем URL, но что из себя представляет поиск представлений?

Необходимость в поиске представлений такова: может быть несколько действий, которые вы можете выполнить после того, как ресурс будет найден. В нашем примере с фотографиями вы можете посмотреть фотографию на странице, но вы также можете захотеть предоставить способ редактирования фотографии и сопутствующей ей мета-информации. Первое представление мы назовем view, а второе будет называться edit. (Оригинально, я знаю.) Pyramid имеет централизованный реестр представлений где именованные представления могут быть проассоциированны со специфичными типами ресурсов. То есть в нашем примере мы предполагаем то, что мы зарегистрировали представления view и edit для объекта «фотография» и мы указали, что представление view является представлением по умолчанию. Путь /joeschmoe/photos/photo1/view тождественен пути /joeschmoe/photos/photo1. Представление редактирования будет доступно по запросу /joeschmoe/photos/photo1/edit.

Надеемся на то, что понятно, что первая часть часть URL будет возвращать тот-же самый ресурс, что и версия чуть выше, которая не имеет возможности редактирования фотографии, а именно ресурс возвращаемый по вызову get_root()['joeschmoe']['photos']['photo1']. Но траверс заканчивается здесь. photo1 не имеет ключа edit. Фактически он (объект типа «фотография») даже может и не быть словарным объектом, в котором photo1['edit'] будет бессмысленным. Когда поиск ресурсов в Pyramid будет закончен и будет найден конечный фрагмент дерева (нужный ресурс), но весь путь запроса все еще не кончился, то следующие сегменты будут трактоваться как названия представлений. Реестр далее будет проверять является ли нужное представление проассоциированным с ресурсом данного типа. Если так, то представление будет вызвано с ресурсом, переданным как соотвествующий контекстный объект (также доступный как request.context). Если представление для вызова не будет найдено, то Pyramid просто вернет ответ 404 Not Found.

Можно переписать запрос /joeschmoe/photos/photo1/edit в следующий кусок питонического псевдокода::

  context = get_root()['joeschmoe']['photos']['photo1']
  view_callable = get_view(context, 'edit')
  request.context = context
  view_callable(request)

Функций get_root() и get_view() не существует на самом деле. Внутри себя, Pyramid работает немного иначе и сложнее. Однако пример выше является разумным приближением алгоритма поиска вьюшек в псевдокоде.

Применения
---------

Почему мы должны думать о траверсе? URL матчинг проще пояснить и он достаточно хорош, верно?

В некоторых случах, да, но, конечно, не во всех случаях. До сих пор у нас были очень структурированные URLы, где наш путь имел специфичные, маленькие кусочки::

  /{userid}/{typename}/{objectid}[/{view_name}]

Во всех этих примерах до сих пор мы захардкодивали название определенного кусочка, предполагая, что мы знаем во время разработки какие имена будут использоваться (photos, blog и так далее). Но что если мы не знаем какие имена это будут в итоге? Или, что еще хуже, что если мы не знаем вообще ничего о будущей структуре URL внутри директории пользователя? Мы можем писать CMS в которой мы хотим, чтобы конечный пользователь имел возможность произвольно добавлять содержимое и другие директории внутри его директории. Он может решить сделать иерархию глубиной в дюжину. Какими будут ваши шаблоны сопоставления в классическом роутинге, которые позволят каждой учетной записи пользователя использовать любые комбинации путей?

Это вполне возможно и реализуемо, но конечно это будет не так-то просто. Шаблоны сопоставления будут усложняться очень быстро по мере того, как вы будете пытаться учесть все тонкости и случаи расширяемой структуры директорий пользователя.

С траверсом, однако, это очень просто и логично. Двадцать слоев иерархии не будет проблемой. Pyramid с удовольствием сделает вызов __getitem__ столько раз, сколько надо до тех пор пока не кончится сегменты пути или пока ресурс создаст исключение KeyError. Каждый ресурс должен знать только лишь то, как получить его непосредственных потомков на один уровень ниже (дети), обо всем остальном позаботится алогоритм траверса. И еще, так как структура дерева ресурсов может находится в базе данных, а не в коде, то будет очень просто дать пользователям возможность модифицировать дерево во время исполнения для установки персонализированной структуры директорий.

Другой случай применения траверса, где он покажет себя очень хорошо, это там, где нужна поддержка контекстно-зависимых политик безопасности. Примером может быть система документооборота для огромной корпорации, где члены разных департаментов имеют разные уровни доступа к документам и файлам других различных департаментов. Разумно, что мы должны уметь каждому файлу по-отдельности также задавать права для отдельных групп или отдельных пользователей пользователей. Траверс показывает себя в такой ситуации очень хорошо если ваши ресурсы фактически представляют объекты данных относящихся к вашим документам, потому как основная идея авторизации ресурсов непосредственно связана с разрешением кода и процесса вызова. Объекты-ресурсы могут хранить списки доступов ACL, которые могут быть унаследованы или переопределены подресурсами или надресурсами.

Если каждый ресурс будет генерировать контекстно-ориентированные ACL, тогда код представления может попытаться выполнить нужное действие и проверит перед этим через ACL может ли текущий пользователь совершить это действие. Таким образом вы достигаете instance based или row level безопасности, которую значительно более сложно реализовать стандартным табличным способом и классическом роутингом. Pyramid активно поддерживает такие схемы и фактически если вы регистрируете ваши вьюшки с правами защиты и используете авторизационную политику, Pyramid может проверять через ACL и решать доступна ли или нет текущая вьюшка текущему пользователю.

Подводя итог, можно сказать, что существует целый класс проблем которые легко решаются путем траверса и поиска представлений, чем через классический роутинг. Если ваши проблемы не требуют этого, отлично: продолжайте работать дальше по классической схеме роутинга, но если вы используете Pyramid и вы понимаете, что вам нужно будет работать с одним из таких случаев, то вы будете рады иметь механизм траверса в вашем инструменте.

Более того, возможно смешение и сочетание траверса с классическим роутингом в одном и том-же Pyramid приложении.

.. note:: Можно смешивать траверс и URL диспатч в одном и том же приложении :app:`Pyramid` application. Почитайте главу
   :ref:`hybrid_chapter` для более подробной информации.
   
.. note:: Перевод: Тимур Рузиев aka resurtm
