.. _index:

=================================================
Pyramid - Web-фреймворк
=================================================

:app:`Pyramid` это маленький, быстрый, практичный Python фреймворк,
для разработки веб приложений.  Он разрабатывается, как часть `Проекта Pylons
<http://docs.pylonsproject.org/>`_.  И лицензируется, по `BSD-подобной лицензии
<http://repoze.org/license.html>`_.

Вступление
============

.. toctree::
   :maxdepth: 1

   copyright.rst
   conventions.rst

Что нового ?
======================

.. toctree::
   :maxdepth: 2

   whatsnew-1.0

Общая документация
=======================

Документация описывает использование фреймворка
:app:`Pyramid`.

.. toctree::
   :maxdepth: 2

   narr/introduction
   narr/install
   narr/configuration
   narr/firstapp
   narr/project
   narr/startup
   narr/urldispatch
   narr/muchadoabouttraversal
   narr/traversal
   narr/views
   narr/renderers
   narr/templates
   narr/viewconfig
   narr/resources
   narr/assets
   narr/webob
   narr/sessions
   narr/security
   narr/hybrid
   narr/i18n
   narr/vhosting
   narr/events
   narr/environment
   narr/testing
   narr/hooks
   narr/advconfig
   narr/extending
   narr/router
   narr/threadlocals
   narr/zca

Руководства
=========

Детализированные руководства рассказывают как создавать 
различные типы приложений, с помощью  :app:`Pyramid`,
и как развертывать их на разных платформах.

.. toctree::
   :maxdepth: 2

   tutorials/wiki/index.rst
   tutorials/wiki2/index.rst
   tutorials/bfg/index.rst
   tutorials/gae/index.rst
   tutorials/modwsgi/index.rst

Справочный материал
==================

Справка включает в себя сведения о всех API :app:`Pyramid`.

.. toctree::
   :maxdepth: 2

   api

Детализированная история изменений
=======================

.. toctree::
   :maxdepth: 1

   changes

Архитектура Pyramid
====================

.. toctree::
   :maxdepth: 1

   designdefense

Примеры приложений
===================

`cluegun <https://github.com/Pylons/cluegun>`_ это pastebin-like
сервис основанный на Rocky Burt's `ClueBin
<http://pypi.python.org/pypi/ClueBin/0.2.3>`_.  Он демонстрирует
обработку форм, безопасность, и использование:term:`ZODB` без :app:`Pyramid`
Посмотрите на код этого приложения, с помощью :

.. code-block:: text

  git clone git://github.com/Pylons/cluegun.git

`virginia <https://github.com/Pylons/virginia>`_ это очень простой
файл рендер.  Он может покзывать документы Stuctured Text, 
HTML файлы, и изображения из папки.
Ранние версии приложения работали на  `repoze.org
<http://repoze.org>`_.  Посмотрите на код этого приложения, с помощью :

.. code-block:: text

  git clone git://github.com/Pylons/virginia.git

`shootout <https://github.com/Pylons/shootout>`_ это пример 
"идейного" приолжения от Carlos de la Guardia.  Оно демонстрирует
гибрид :term:`URL dispatch` и :term:`traversal`, интегрированного с
`SQLAlchemy <http://www.sqlalchemy.org/>`_, :term:`repoze.who`, и
`Deliverance <http://www.deliveranceproject.org/>`_.  
Посмотрите на код этого приложения, с помощью :

.. code-block:: text

  git clone git://github.com/Pylons/shootout.git

Устаревшие примеры приложений (repoze.bfg)
======================================

.. note::

   Эти приложения написанны на старой версии :app:`Pyramid`, которя
   называлась :mod:`repoze.bfg`.  Они не могут работать без дополнительной модификации под :app:`Pyramid`,
   могут дать полезные представления.

`bfgsite <http://svn.repoze.org/bfgsite/trunk>`_ это приложение,
на котором работает`bfg.repoze.org <http://bfg.repoze.org>`_ Вебсайт.
Оно демонстрирует интеграцию с Trac, и включает в себя нескольно
мини-приложений, таких как pastebin и движок мануалов.
Посмотреть код проекта на SVN, можно так :

.. code-block:: text

  svn co http://svn.repoze.org/buildouts/bfgsite/ bfgsite_buildout

`KARL <http://karlproject.org>`_ это довольно большое
(примерно 70k строк кода) основанное на  :mod:`repoze.bfg`
и других приложениях Repoze.  Это OpenSource web-система, для
совместной работы, корпоративных сетей, и баз знаний.
Оно предостовляет функциональность вики, календарей, руководств,
поиска, тэггирования, комментирования, и загрузки файлов.
Посмотрите `Сайт KARL<http://karlproject.org>`_, для скачивания и деталей установки.

Поддержка и Разроботка
=======================

`Сайт Проекта Pylons <http://pylonsproject.org/>`_ это главный онлайн источник 
информации о :app:`Pyramid`.

Для сообщения о ошибках, используйте issue tracker
<http://github.com/Pylons/pyramid/issues>`_.

Если у вас появились вопросы, не освещенные в данной документации
свяжитесь в рассылкой `Pylons-devel
<http://groups.google.com/group/pylons-devel>`_ или присоеденитесь к `#pylons
IRC каналу <irc://irc.freenode.net/#pylons>`_.

Посмотрите на тэгированные и нестабильные версии :app:`Pyramid` с помощью
`репозитория Pyramid на GitHub <http://github.com/Pylons/pyramid/>`_.
Что бы посмотреть нестабильный код на ``git``, используйте эту комманду:

.. code-block:: text

  git clone git@github.com:Pylons/pyramid.git

Что-бы узнать как стать контрибутором :app:`Pyramid`, посмотрите
`эту секцию документации
<http://docs.pylonsproject.org/index.html#contributing>`_.

Индекс и Глоссарий
==================

* :ref:`glossary`
* :ref:`genindex`
* :ref:`search`
