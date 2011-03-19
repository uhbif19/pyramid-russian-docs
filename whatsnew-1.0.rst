
Что нового в Pyramid 1.0

Что нового в Pyramid 1.0
=========================


Эта статья описывает различия между Pyramid версии 1.0, по сравнению с его предшественником :mod:`repoze.bfg` 1.3. Она также описывает обратные несовместимости, между двумя версиями, изменения зависимостей и документации.

Основные изменения
-----------------------

Главные изменения в Pyramid 1.0 это :

- Новое имя и брэнд связанный с проектом Pylons.

- Скрипт перехода с BFG

- Изменения в шаблонах Paster

- Изменения терминологии

- Лучшая совместимость  и поддержка

- Встроенная поддержка языка шаблонов Mako

- Встроенная поддержка сессий

- Обновленные возможности  URL диспатчинга

- Лучшая поддержка императивной конфигурации

 - ZCML

 - Лучшая поддержка глобальных переменных во время рендеринга

- View mappers

- Обновленная система тестирования

- Поддержка аутентификации

- Возможности документирования

Новое имя и бренд
~~~~~~~~~~~~~~~~~~~~~

Имя из ``repoze.bfg``поменялось на Pyramid. 
Так-же проект теперь является подпроектом, новой сущности - Проекта Pylons. Проект Pylons, это коллекция связанных с веб-программированием технологий. Pyramid стал первым пакетом Проекта Pylons. Другие пакеты, полезные как для пользователей Pylons 1.0, так и для приверженцев Zope, добавляются с течением времени.
Pyramid это наследник, как  :mod:`repoze.bfg`, так и :term:`Pylons` версии 1.0 .


Большая часть кодовой базы Pyramid взята из :mod:`repoze.bfg`, с некоторыми дополнительными изменениями, для совместимости в Pylons 1.

Технически Pyramid несовместим с :mod:`repoze.bfg`, он имеет новое имя, так что старые импорты модулей ``repoze.bfg`` выдадут ошибку. 
Тем не менее, вам не нужно сделать не так много, чтобы запустить ваши BFG приложения под Pyramid. Есть автоматизированный скрипт, который поменяет большинство импортов и ZCML деклараций. Посмотрите http://docs.pylonshq.com/pyramid/dev/tutorials/bfg/ для инструкций по обновлению.

Пользователям Pylons 1, нужно будет больше поработать, для использования Pyramid, так как нету автоматических средств преобразования для Pylons. Надеемся, что с течением времени появится больше документации и кода, для облегчения перехода с Pylons 1.

:mod:`repoze.bfg` версии 1.3 это последний крупный релиз. Апдейты будут выходить только для баг-фиксов. Pylons 1 продолжит развитие.

Проект Repoze продолжит существовать. Repoze сможет заняться своей основной деятельностью: переносом Zope технологий в  WSGI. Популярность фреймворка :mod:`repoze.bfg`, самого по себе препятствует этому.

Мы надеемся, что людей привлекло чувство сотрудничества, присущее Проекту Pylons и объединение комьюнити. Теряя немного суверенитета, мы получаем возможность работать вместе. В противоположность к этому, создание форков и разделение проектов является более распространенной практикой в мире опенсурс. Мы чувствуем что в пространстве веб-фреймворков первого уровня, не так много места. Объедения несколько проектов, с похожей философией мы получаем больше шансов на успех. 

Скрипт преобразования из BFG
~~~~~~~~~~~~~~~~~~~~~

Скрипт ``bfg2pyramid``, позволяет в большинстве случаев автоматически преобразовать существующее :mod:`repoze.bfg` в Pyramid. Этот процесс описан в :ref:`converting_a_bfg_app`.

Изменения шаблонов  Paster 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Новая графика и CSS

 - Файл ``development.ini`` сконфигурирован, для использования  :term:`WebError` по умолчанию.

- Все шаблоны Paster теперь сведены к норме. Каждый теперь использует название ``main``, для функции которая возвращает WSGI приложение. Стандартизирован стиль файла ``development.ini`` .

- Все предшествующие шаблоны Paster теперь используют императивную конфигурацию (``starter``, ``routesalchemy``, ``alchemy``, ``zodb``), вместо ZCML.

- The ``pyramid_zodb``, ``pyramid_routesalchemy`` and ``pyramid_alchemy``
  paster templates now use a default "commit veto" hook when configuring the
  ``repoze.tm2`` transaction manager in ``development.ini``.  This prevents a
  transaction from being committed when the response status code is within
  the 400 or 500 ranges.  See also
  http://docs.repoze.org/tm2/#using-a-commit-veto.

Смена терминологии
~~~~~~~~~~~~~~~~~~~

- Концепт ранее известный как "модель", теперь называется "ресурс". В результате, соответствующие API переименовываются. Для совместимости старые понятия были оставлены::

pyramid.url.model_url -> 
pyramid.url.resource_url

pyramid.traversal.find_model -> 
pyramid.url.find_resource

pyramid.traversal.model_path ->
pyramid.traversal.resource_path

pyramid.traversal.model_path_tuple ->
pyramid.traversal.resource_path_tuple

pyramid.traversal.ModelGraphTraverser -> 
pyramid.traversal.ResourceTreeTraverser

pyramid.config.Configurator.testing_models ->
pyramid.config.Configurator.testing_resources

pyramid.testing.registerModels ->
pyramid.testing.registerResources

pyramid.testing.DummyModel ->
pyramid.testing.DummyResource

- Вся документация теперь содержит новую терминологию.

- Шаблон ``starter`` теперь имеет модуль ``resources.py``, вместо ``models.py``.

- В названиях аргументов различных API, также ``model`` сменено на ``resource``.

- Концепт называвшийся "resource", теперь называется "asset". Обратная совместимость оставлена, в рамках необходимости::

pyramid.config.Configurator.absolute_resource_spec ->
pyramid.config.Configurator.absolute_asset_spec


pyramid.config.Configurator.override_resource ->
pyramid.config.Configurator.override_asset

- Модуль (не-API) ``pyramid.resource`` заменен ``pyramid.asset``.

- All docs that previously referred to "resource specification" now refer
  to "asset specification".

- Установка ``BFG_RELOAD_RESOURCES`` (envvar) или ``reload_resources`` (конфигурационный файл), теперь называются  ``PYRAMID_RELOAD_ASSETS`` и ``reload_assets`` соответственно.

Улучшенная совместимость и документация
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Pyramid запускается как на Jython, так и на PyPy.
Тем не менее Chameleon не работает на обоих, но вы можете использовать шаблонизаторы Mako или Jinja2 на этих платформах.

Сессии
~~~~~~~~


Теперь Pyramid имеет встроенную поддержку сессий, документированную в :ref:`sessions_chapter`. Конкретные реализации сессий можно подключать. Также поддерживается flash-сообщения и защита от XSS.

``request.session`` это (dict-подобный) обьект сессия, если :term:`session factory` сконфигурировано.

Добавлен новый аргумент ``session_factory`` к конструктору Configurator-а, и новый метод :meth:`pyramid.config.Configurator.set_session_factory`.

Mako
~~~~

В добавок к шаблонизатору Chameleon, Pyramid имеет встроенную поддержку :term:`Mako`. Посмотрите :ref:`mako_templates` для дополнительной информации.

URL Dispatch
~~~~~~~~~~~~

- URL Dispatch теперь поддерживает маркеры везде, а не только сразу после ``/``.

- URL Dispatch теперь использует запись  ``{marker}`` вместо ``:marker``. Старый синтаксис маркеров, все еще доступен в целях совместимости. Новый формат поддерживает регулярные выражения в маркерах, вместо стандартного ``[^/]+``, например  ``{marker:\d+}`` маркер из цифр.

- Addded a new API :func:`pyramid.url.current_route_url`, which computes a
  URL based on the "current" route (if any) and its matchdict values.

- Добавлена команда ``paster proute``, которая показывает всю имеющеюся таблицу роутинга. Почитайте документацию :ref:`displaying_application_routes`.

- Added ``debug_routematch`` configuration setting (settable in your ``.ini``
  file) that logs matched routes including the matchdict and predicates.

- Добавлена функция :func:`pyramid.url.route_path`, которая генерирует относительные URL-ы. Вызов ``route_path`` это то же самое, что и вызов :func:`pyramid.url.route_url` с аргументом ``_app_url`` равным пустой строке.

- Добавлено API :meth:`pyramid.request.Request.route_path`. Это вспомогательный метод request-обьекта, который вызывает :func:`pyramid.url.route_url`.

- Добавлены поля ``matchdict`` и ``matched_route`` к :class:`pyramid.request.Request`. Каждый из них устанавливается в ``None`` когда роутинг не произведен во время запроса.

Вынесение ZCML в отдельный модуль
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Метод ``load_zcml`` класса Configurator был удален из Pyramid.  Загрузка ZCML это теперь прерогатива пакета :term:`pyramid_zcml`, который может быть загружен из PyPI.
Документация пакета доступна в http://pylonsproject.org/projects/pyramid_zcml/dev/, где описывается как добавить конфигуратор в ваш блок ``main`` чтобы переопределить этот метод. Вам также нужно добавить 
зависимость к ``pyramid_zcml`` в ``install_requires`` вашего 
файла ``setup.py``.

- Глава  "Declarative Configuration" удалена из документации (ее переместили в пакет ``pyramid_zcml``).

- Большинство ссылок на ZCML были перенесены в документацию ``pyramid_zcml``.

- Шаблон ``starter_zcml`` перемещен в пакет ``pyramid_zcml``.

Императивная Конфигурация
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для поддержки расширяемости приложений :term:`Configurator` :app:`Pyramid`, по умолчанию, определяет конфликты конфигурации и позволяет подгружать императивную конфигурацию из других пактов и модулей. Также по умолчанию конфигурация делится на две независимые фазы. Это позволяет игнорировать релятивную конфигурацию в некоторых ситуациях. Посмотрите :ref:`advconfig_narr` для дополнительной информации.

Метод :meth:`pyramid.config.Configurator.add_directive`  позволяет делать расширения конфигуратора добавлением методов, чтобы избежать наследования Configurator-а просто для добавления методов. Посмотрите :ref:`add_directive` для информации.

Больше нет необходимости обрамлять конфигурацию ``config.begin()`` и  ``config.end()``. Все шаблоны paster больше не используют эти функции.

Лучшая поддержка глобальных переменных при рендеринге

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Новый тип событий :class:`pyramid.interfaces.IBeforeRender` теперь посылается перед рендерингом. Приложения могут подписываться на событие ``IBeforeRender``, чтобы изменить переменные шаблона перед запуском рендерера. Событие имеет dict-подобный интерфейс который может быть использован для этих целей. К примеру::

from repoze.events import subscriber
from pyramid.interfaces import IRendererGlobalsEvent

@subscriber(IRendererGlobalsEvent)
def add_global(event):
event['mykey'] = 'foo'

View Mappers
~~~~~~~~~~~~

Система вью-мапперов расширена и позволяет фреймворку контролировать как вызываемые-обьекты были созданы и использованны. Посмотрите :ref:`using_a_view_mapper`, для дополнительной информации.

Улучшения возможностей тестирования
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функции `pyramid.testing.setUp` и :func:`pyramid.testing.tearDown` снова актуальны. Теперь это стандартные API, для конфигурации тестирования. Это изменение сделано для создания абстракции, которая защитит от дальнейших изменений API Configurator-а.

Аутентификация
~~~~~~~~~~~~~~~ 

- Интерфейс :class:`pyramid.interfaces.IAuthenticationPolicy` теперь содержит метод ``unauthenticated_userid``. Этот метод нужен людям, которые используют хранилища не поддерживающие кэширования обьектов, и хотят создать "user object" как атрибут запроса.

- Новое API добавлено к модулю :mod:`pyramid.security`, функция :mod:`pyramid.security`. Она вызывает метод ``unauthenticated_userid``.

- Класс :class:`pyramid.authentication.AuthTktCookieHelper`  теперь входит в API. Этот класс может быть использован для внешних политик безопасности, разработанных для помощи в установке Cookies.

- Класс :class:`pyramid.authentication.AuthTktAuthenticationPolicy` теперь принимает параметр `tokens`` с помощью функции :func:`pyramid.security.remember`. Значение должно быть последовательностью строк. Токены также добавляются в поле auth_tkt и возвращаются в auth_tkt Cookie.

-  Добавлен аргумент ``wild_domain`` в класс :class:`pyramid.authentication.AuthTktAuthenticationPolicy`, по умолчанию установленный в ``True``. Если установить его в ``False``,  то политика безопасности которая устанавливает cookie с wildcard доменом, отключается.

Улучшения Документации
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Глава "Resource Location and View Lookup" была  на заменена на статью Роба Миллера "Much Ado About Traversal" 
(оригинал http://blog.nonsequitarian.org/2010/much-ado-about-traversal/).

- Множество пользователей внесли изменения в документацию.

Мелкие Изменения
----------------------------

- Словарь ``settings`` был поглощен классом Configurator, и доступен как ( ``config.registry.settings`` в коде конфигурации и ``request.registry.settings`` в коде view-ов ).

- Метод :meth:`pyramid.config.Configurator.add_view` теперь принимает  именованный аргумент ``decorator``, функцию которой нужно декорировать view, перед его добавлением в рееестр.

- Allow static renderer provided during view registration to be overridden at
  request time via a request attribute named ``override_renderer``, which
  should be the name of a previously registered renderer.  Useful to provide
  "omnipresent" RPC using existing rendered views.

- Если ресурс определил метод ``__resource_url__``, то его вызовут в результате применения :func:`pyramid.url.resource_url` для создания url не соответствующего стандартной логике.  Для дополнительной информации почитайте :ref:`generating_the_url_of_a_resource`.

-  Имя  ``registry`` теперь доступно в окружении ``pshell``.

- Добавлена поддержка json на  Google App Engine, через обработку исключения :exc:`NotImplementedError` и импорта ``simplejson`` из ``django.utils``.

- Добавлен модуль :mod:`pyramid.httpexceptions`, который является синонимом к ``webob.exc``.

- Новый класс  class:`pyramid.response.Response`. Это синоним к ``webob.Response`` (старый код не должен изменятся на использование этого имени, оно создано в основном для целей документации).

- Request теперь имеет новый атрибут ``tmpl_context`` , для удобства пользователей Pylons.

- Новые API :class:`pyramid.request.Request`: ``model_url``,
``route_url`` и  ``static_url``. Это простые ссылки на соответствующие им ссылки в :mod:`pyramid.url`.

Обратная несовместимость
------------------------------------

- Когда совершена ошибка :class:`pyramid.exceptions.Forbidden` ее HTTP код статуса сейчас `403 Forbidden``. Раньше же он был ``401 Unauthorized``, для обратной совместимости с :mod:`repoze.bfg`. Изменение может вызвать проблемы у пользователей :mod:`repoze.who`. Им необходимо сконфигурировать  :mod:`repoze.who` на взаимодействие с ``403 Forbidden``.. Сделать это используя ``challenge_decider`` можно так::

import zope.interface
from repoze.who.interfaces import IChallengeDecide

def challenge_decider(environ, status, headers):
return status.startswith('403') or status.startswith('401')
zope.interface.directlyProvides(challenge_decider, IChallengeDecider)

- Команда ``paster bfgshell`` переименована в ``paster pshell``.

- Больше нет объекта ``IDebugLogger``. Теперь он зарегистрирован, как утилита ``repoze.bfg.debug``.

- Следующие API были удалены :
``pyramid.testing.registerViewPermission``,
``pyramid.testing.registerRoutesMapper``, ``pyramid.request.get_request``,
``pyramid.security.Unauthorized``,
``pyramid.view.view_execution_permitted``, ``pyramid.view.NotFound``

- The Venusian "category" for all built-in Venusian decorators
  (e.g. ``subscriber`` and ``view_config``/``bfg_view``) is now
  ``pyramid`` instead of ``bfg``.

Функция ``pyramid.renderers.rendered_response``  заменена на :func:`pyramid.renderers.render_to_response`.

- Renderer factories now accept a *renderer info object* rather than an
  absolute resource specification or an absolute path.  The object has the
  following attributes: ``name`` (the ``renderer=`` value), ``package`` (the
  'current package' when the renderer configuration statement was found),
  ``type``: the renderer type, ``registry``: the current registry, and
  ``settings``: the deployment settings dictionary.  Third-party
  ``repoze.bfg`` renderer implementations that must be ported to Pyramid will
  need to account for this.  This change was made primarily to support more
  flexible Mako template rendering.

- Предназначение ``repoze.bfg.message`` теперь устарело. Используйте атрибут ``exception`` запроса (к примеру  ``request.exception[0]``) чтобы передать сообщение.

- Значения ``bfg_localizer`` и ``bfg_locale_name`` сохраняются при запросе во время интернализации для целей новоых API. Они заменены на ``localizer`` и ``locale_name``, соответственно.

- The default ``cookie_name`` value of the
  :class:`pyramid.authentication.AuthTktAuthenticationPolicy` now defaults to
  ``auth_tkt`` (it used to default to ``repoze.bfg.auth_tkt``).

- Функция :func:`pyramid.testing.zcml_configure` удалена. Ее удаление было анонсировано еще в  :mod:`repoze.bfg` 1.2a1, но в действительности еще не было совершено.

- Переменные окружения начинавшиеся на  ``BFG_`` теперь начинаются на ``PYRAMID_`` (например `BFG_DEBUG_NOTFOUND`` теперь
``PYRAMID_DEBUG_NOTFOUND``)

- Теперь реализация интерфейса :class:`pyramid.interfaces.IAuthenticationPolicy`  обязана определять метод ``unauthenticated_userid``. Она вызывается, с помощью глобальной функции :func:`pyramid.security.unauthenticated_userid`, так что если вы ее не используете вы не заметите изменений.

- ``configure_zcml`` без каких либо настроек развертывания (**settings), больше не имеет никакого смысла.

- Функция ``make_app`` была удалена из модуля :mod:`pyramid.router`. Она продолжит существовать, но теперь в пакете ``pyramid_zcml``. Это оставляет модуль :mod:`pyramid.router` без каких либо функций API.

Устаревшее
----------------

- Класс :class:`pyramid.configuration.Configurator` объявлен устаревшим. Используйте класс :class:`pyramid.config.Configurator`, с параметром ``autocommit=True``, вместо него. Ссылка :class:`pyramid.configuration.Configurator`  будет оставаться долгое время, так как его использует каждое приложение. Но его импорт будет вызывать предупреждение, об устаревшей функции. :class:`pyramid.config.Configurator`  имеет то же API но авто-коммит отключен, по умолчанию. ``pyramid.configuration.Configurator`` же совершает коммит, после каждого изменения конфигурации.

- Функция func:`pyramid.settings.get_settings`  устарела. Используйте ``pyramid.threadlocals.get_current_registry().settings``  вместо нее. Так же вы можете использовать поле ``settings``  доступное из request-объекта (``request.registry.settings``).


- Декоратор ранее известный как ``pyramid.view.bfg_view``, теперь называется более формально :class:`pyramid.view.view_config`.

- Obtaining the ``settings`` object via
  ``registry.{get|query}Utility(ISettings)`` is now deprecated.  Instead,
  obtain the ``settings`` object via the ``registry.settings`` attribute.  A
  backwards compatibility shim was added to the registry object to register
  the settings object as an ISettings utility when ``setattr(registry,
  'settings', foo)`` is called, but it will be removed in a later release.

- Доступ к объекту ``settings``, через :func:`pyramid.settings.get_settings` устарел. Теперь используйте для этого поле ``settings`` реестра ( доступ к реестру через :func:`pyramid.threadlocal.get_registry` или``request.registry``). 

Изменение зависимостей
----------------------------------

Требуется Venusian >= 0.5.

Улучшения документации
------------------------------------

- Добавлена глава документации API :mod:`pyramid.httpexceptions`.

- Добавлена глава документации API :mod:`pyramid.session` .

- Добавлена глава :mod:`pyramid.response`.

- Добавлена глава :ref:`sessions_chapter` в руководство.

- Вся документация ссылавшаяся на  ``webob.Response``, теперь использует :class:`pyramid.response.Response`.

- Документация использует императивную конфигурацию, ведь теперь декларативная (ZCML) выделена во внешний пакет :term:`pyramid_zcml`.

- Удалена глава ``zodbsessions``. Их все еще можно использовать, но теперь появилась абстракция SessionFactory которая выполняет те же функции и разработка документации в обоих направлениях нецелесообразна.

- Добавлен пример функционального тестирования ``WebTest`` в руководство, глава  :ref:`functional_tests`.

- Расширенна глава Ресурсы, примерами вызовов ресурсо-зависимых API.

- Добавили  "Pyramid Provides More Than One Way to Do It"  к документации архитектуры.

- Руководство "Converting a CMF Application to Pyramid" было удалено из секции руководств и перемещено в репозиторий ``pyramid_tutorials``.

-Статьи "Using ZODB With ZEO" и "Using repoze.catalog Within Pyramid" перемещены из основной документации в Pyramid Tutorials.

- Удалена документация для устаревших API модуля ``pyramid.testing`` :
``registerDummySecurityPolicy``, ``registerResources``, ``registerModels``,
``registerEventListener``, ``registerTemplateRenderer``,
``registerDummyRenderer``, ``registerView``, ``registerUtility``,
``registerAdapter``, ``registerSubscriber``, ``registerRoute``, и
``registerSettings``.


-------------------------------------------------------------------------------
http://translated.by/you/what-s-new-in-pyramid-1-0/into-ru/trans/
Оригинал (английский): What’s New In Pyramid 1.0 (http://docs.pylonsproject.org/projects/pyramid/1.0/whatsnew-1.0.html)
Перевод: © uhbif19, ma832.
Лицензия: Creative Commons

translated.by переведено толпой