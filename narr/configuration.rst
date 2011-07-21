.. index::
	single: application configuration

.. _configuration_narr:

Конфигурация приложения
======================

Каждая установка приложения написанного на :app:`Pyramid` создает специфичную *конфигурацию*. Например приложение хранящие MP3 файлы, подключает код для управления музыкальными файлами. А например приложение для корпоративного использования, может подключать код для управления данными о пользователях. Способ которым код подключается к приложению на :app:`Pyramid` называется "конфигурация".

Большинство людей понимают "конфигурацию", как настройки экземпляра приложения. Например легко думать, что значения определенные в ``.ini`` файле, считываются при запуске приложения как "конфигурация". :app:`Pyramid` расширяет это понятие , называя так стандартные способы подключения внешнего кода. Когда вы подключаете код к :app:`Pyramid` вы "конфигурируете" приложение.

.. index::
	single: imperative configuration

.. _imperative_configuration:

Императивная конфигурация
--------------------------------------------

Вот несколько простейших приложений :app:`Pyramid`, сконфигурированных императивно:

.. code-block:: python
	:linenos:

	from paste.httpserver import serve
	from pyramid.config import Configurator
	from pyramid.response import Response

	def hello_world(request):
	return Response('Hello world!')

	if __name__ == '__main__':
	config = Configurator()
	config.add_view(hello_world)
	app = config.make_wsgi_app()
	serve(app, host='0.0.0.0')

Мы пока не будем обсуждать, что делает приложение. Просто запомните, что конфигурационные выражения вида ``if __name__ ==
'__main__':`` заменяются вызовами методов класса :term:`Configurator` (к примеру ``config.add_view(...)``). Эти утверждения находятся одни за другими, и выполняются в порядке следования.

.. index::
	single: view_config
	single: configuration decoration
	single: code scanning

.. _decorations_and_code_scanning:

Декораторы и обработка кода
--------------------------------------------

Другой вариант конфигурации, делает её более приближенной к самому коду. Иногда сложно держать конфигурацию отдельно, когда код занимает несколько файлов. Тогда, чтобы увидеть проект целостно, вам придется работать с множеством файлов. :app:`Pyramid` позволяет вам избежать этого. К примеру :

.. code-block:: python
	:linenos:

	from pyramid.response import Response
	from pyramid.view import view_config

	@view_config(name='hello', request_method='GET')
	def hello(request):
	return Response('Hello')

Но есть тонкость, что простая декорация не записывает никаких изменений в конфигурации. Для оказания эффекта на конфигурацию, необходимо провести процесс :term:`сканирования`.

Например декоратор :class:`pyramid.view.view_config`, в примере добавляет атрибуты к функции ``hello``, делая их доступными для последующего сканирования.

:term:`Сканирование` модуля какого либо пакета и его под-пакетов на декораторы, происходит когда вызывается метод :meth:`pyramid.config.Configurator.scan`: сканирование запускает поиски конфигурации в пакете. К примеру:

.. topic:: Starting A Scan

.. code-block:: python
	:linenos:

	from paste.httpserver import serve
	from pyramid.response import Response
	from pyramid.view import view_config

	@view_config()
	def hello(request):
	return Response('Hello')

	if __name__ == '__main__':
	from pyramid.config import Configurator
	config = Configurator()
	config.scan()
	app = config.make_wsgi_app()
	serve(app, host='0.0.0.0')

Механизм сканирования импортирует каждый модуль рекурсивно, находя специальные атрибуты обьектов определенных в модуле.Эти атрибуты определяются в коде обыкновенно, с помощью декораторов. Например декоратор :class:`~pyramid.view.view_config` может быть назначен функции или методу.

Когда сканирование запущенно, и декораторы конфигурации найдены сканером, ряд вызовов совершается к классу :term:`Configurator` от вашего имени :они заменяют необходимость делать императивную конфигурацию.

В примере сверху, сканер переводит аргументы class:`~pyramid.view.view_config` в вызовы метода :meth:`pyramid.config.Configurator.add_view`.

.. ignore-next-block
.. code-block:: python

	config.add_view(hello)

Декларативная конфигурация
----------------------------------------------

Третий вид конфигурации :app:`Pyramid` называется *декларативная конфигурация*. Этот режим использует XML базированный язык разметки :term:`ZCML` для конфигурации. ZCML не встроен в Pyramid. Вы можете использовать его, установив пакет :term:`pyramid_zcml`.
