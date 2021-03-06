=====================
 Авторское Вступление
=====================

Добро пожаловать в "Веб-Фреймворк :app:`Pyramid`".  В жтом вступлении, 
я опишу аудиторию этой книги, я опишу содержание этой книги, 
я немного раскажу о происхождении :app:`Pyramid`, 
и поблагодорю некоторых важных, для меня людей.

Я надеюсь Вам понравиться как эта книга, так и фреймворк который
она документирует.

.. index::
   single: book audience

Аудитория
========

Эта книга ориентированна на пользователя, обладающего следующими
признаками :

- По крайней мере небольшой опыт прогр:app:`Pyramid`аммирования :term:`Python`.
- Базовые знания веб протоколов, например HTTP и CGI.

Если вы не попадаете в эти категории, то вы безусловно целевая 
аудитория книги. Но не расстраивайтесь, если вы не имеете необходимых 
знаний, вы можете получить их "на лету".

Python - *отличный* язык, для разроботки приложений;
продуктивно работать на Python не так сложно.  Если вы
уже имеете опыт разроботки, на таких языках как Java, Visual
Basic, Perl, Ruby, или может  C/C++, learning Python быдет простым;
за несколько дней, уже можно достигнуть приемлимой производительности.
Если вы не имели такого опыта, то изучение будет намного сложнее, 
но вам придется очень постараться, чтобы найти "первый язык" лучше
Python-а.

Простота в употреблении терминов Web, принята в этой книге. Например
мы не пытаемся определить URL или строку запроса. Конечно, книга 
обьясняет взаимодействия в терминах протокола HTTP, но она не 
обьясняет его строение в деталях.

.. index::
   single: book content overview

Содержание книги
=================

Книга разделена на три большие части :

:ref:`narrative_documentation`

  Эта часть документации описывает концепты :app:`Pyramid`
  в форме руководства, написаного в основном в разговорном стиле.
  Каждая глава Руководства содержит независимый концепт :app:`Pyramid`.
  Вы можете получить представление о предмете главы, читая книгу 
  не по порядку, или когда вы хотите увидеть подзабытый материал
  во время разроботки приложения.

:ref:`tutorials`

  Каждый туториал содержит пример приложения, или примеры использования
  какого либо понятия :app:`Pyramid`.

:ref:`api_reference`

  Подробное изложение каждого API доступного в  :app:`Pyramid`. 
  Документация API упорядочена в алфавитном порядке, по модулям.

.. index::
   single: repoze.zope2
   single: Zope 3
   single: Zope 2
   single: repoze.bfg genesis
   single: pyramid genesis


История :mod:`repoze.bfg`
================================

До конца 2010 года, :app:`Pyramid` назывался :mod:`repoze.bfg`.

Я написал :mod:`repoze.bfg` после многих лет разроботки веб-приложений, 
с использованием :term:`Zope`. Zope дал мне много опыта:
после целой декады успешных веб-приложений я решил начать разроботку 
своего своего веб-фреймворка.

Бренд Repoze существовал до создания :mod:`repoze.bfg`. Один из первых
пакетов разроботанных, как часть Repoze назывался :mod:`repoze.zope2`.
Этот пакет позволял запускать приложения Zope 2 под :term:`WSGI` 
сервером, без доплнительной модификации. Zope 2 не имел поддержки 
WSGI тогда.

Во время разроботки :mod:`repoze.zope2` я понял что механизм репликации
принятый в Zope -- был медленными и сложными.  Zope 2 разрабатывался 
много лет и полная его эмуляция очень сложна.  Я законцил :mod:`repoze.zope2`
и он Zope 2 достаточно хорошо. Но во время его разроботки мне стало ясно, что
Zope 2 слишком сложный, и я начал искать более простые варианты.

Я пробовал использовать Zope 3, но она не сильно продвинулась в 
вопросе упрощения ахитектуры. Я такжен пробовал Django и Pylons, 
но ни один из них не обеспечивал поддержку traversal, декларативного 
описания защиты, расширяемости приложений; это вещ к кторым я уже
привык, как разроботкик Zope.

Моей целью, было создать платформу простую и при этом сохраняющую 
возможности Zope, избавленную от ограничений и алогичностей других
фреймворков.


Происхождение:app:`Pyramid`
=============================

То что :mod:`repoze.bfg` стал называться :app:`Pyramid` это результат
обьединения команд :term:`Repoze` и :term:`Pylons`в 2010 году. 
Мы обьеденили наши нароботки, что-бы не дублировать усилия и 
больше взаимодействовать с другими технологиями.

.. index::
   single: Bicking, Ian
   single: Everitt, Paul
   single: Seaver, Tres
   single: Sawyers, Andrew
   single: Borch, Malthe
   single: de la Guardia, Carlos
   single: Brandl, Georg
   single: Oram, Simon
   single: Hardwick, Nat
   single: Fulton, Jim
   single: Moroz, Tom
   single: Koym, Todd
   single: van Rossum, Guido
   single: Peters, Tim
   single: Rossi, Chris
   single: Holth, Daniel
   single: Hathaway, Shane
   single: Akkerman, Wichert
   single: Laflamme, Blaise
   single: Laflamme, Hugues
   single: Bangert, Ben
   single: Duncan, Casey
   single: Orr, Mike
   single: Shipman, John
   single: Beelby, Chris

Благодарности
==============

Эта книга посвящается моей бабушки, которая подрила мне первую мою
печатную машинку (Royal), и моей маме, которая купила мне первый компьютер
(VIC-20).

Выражаю свою благодарность следующим людям за их экспертную окенку, силы и 
программы. Без них не было бы ни этой книги, ни того о чем она повествует: 
Paul Everitt, Tres Seaver, Andrew Sawyers, Malthe Borch, Carlos de la Guardia,
Chris Rossi, Shane Hathaway, Daniel Holth, Wichert Akkerman, Georg Brandl,
Blaise Laflamme, Ben Bangert, Casey Duncan, Hugues Laflamme, Mike Orr,
John Shipman, Chris Beelby, Simon Oram, Nat Hardwick, Ian Bicking, Jim Fulton,
Tom Moroz of the Open Society Institute, and Todd Koym of Environmental Health Sciences.

Спасибо Гвидо ван Россуму и Тиму Петерсу за Python.

Особая благодарность Триссии, за то что она меня выносит.
