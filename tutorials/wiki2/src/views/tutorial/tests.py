import unittest

from pyramid import testing

def _initTestingDB():
    from tutorial.models import DBSession
    from tutorial.models import Base
    from sqlalchemy import create_engine
    engine = create_engine('sqlite://')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return DBSession

def _registerRoutes(config):
    config.add_route('view_page', '{pagename}')
    config.add_route('edit_page', '{pagename}/edit_page')
    config.add_route('add_page', 'add_page/{pagename}')

class ViewWikiTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def _callFUT(self, request):
        from tutorial.views import view_wiki
        return view_wiki(request)

    def test_it(self):
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        response = self._callFUT(request)
        self.assertEqual(response.location, 'http://example.com/FrontPage')

class ViewPageTests(unittest.TestCase):
    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()
        
    def _callFUT(self, request):
        from tutorial.views import view_page
        return view_page(request)

    def test_it(self):
        from tutorial.models import Page
        request = testing.DummyRequest()
        request.matchdict['pagename'] = 'IDoExist'
        page = Page('IDoExist', 'Hello CruelWorld IDoExist')
        self.session.add(page)
        _registerRoutes(self.config)
        info = self._callFUT(request)
        self.assertEqual(info['page'], page)
        self.assertEqual(
            info['content'], 
            '<div class="document">\n'
            '<p>Hello <a href="http://example.com/add_page/CruelWorld">'
            'CruelWorld</a> '
            '<a href="http://example.com/IDoExist">'
            'IDoExist</a>'
            '</p>\n</div>\n')
        self.assertEqual(info['edit_url'],
                         'http://example.com/IDoExist/edit_page')
        
    
class AddPageTests(unittest.TestCase):
    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()
        self.config.begin()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def _callFUT(self, request):
        from tutorial.views import add_page
        return add_page(request)

    def test_it_notsubmitted(self):
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        request.matchdict = {'pagename':'AnotherPage'}
        info = self._callFUT(request)
        self.assertEqual(info['page'].data,'')
        self.assertEqual(info['save_url'],
                         'http://example.com/add_page/AnotherPage')
        
    def test_it_submitted(self):
        from tutorial.models import Page
        _registerRoutes(self.config)
        request = testing.DummyRequest({'form.submitted':True,
                                        'body':'Hello yo!'})
        request.matchdict = {'pagename':'AnotherPage'}
        self._callFUT(request)
        page = self.session.query(Page).filter_by(name='AnotherPage').one()
        self.assertEqual(page.data, 'Hello yo!')

class EditPageTests(unittest.TestCase):
    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def _callFUT(self, request):
        from tutorial.views import edit_page
        return edit_page(request)

    def test_it_notsubmitted(self):
        from tutorial.models import Page
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        request.matchdict = {'pagename':'abc'}
        page = Page('abc', 'hello')
        self.session.add(page)
        info = self._callFUT(request)
        self.assertEqual(info['page'], page)
        self.assertEqual(info['save_url'],
                         'http://example.com/abc/edit_page')
        
    def test_it_submitted(self):
        from tutorial.models import Page
        _registerRoutes(self.config)
        request = testing.DummyRequest({'form.submitted':True,
                                        'body':'Hello yo!'})
        request.matchdict = {'pagename':'abc'}
        page = Page('abc', 'hello')
        self.session.add(page)
        response = self._callFUT(request)
        self.assertEqual(response.location, 'http://example.com/abc')
        self.assertEqual(page.data, 'Hello yo!')
