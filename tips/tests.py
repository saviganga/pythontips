from django.test import TestCase
from .models import Tweet, MyUser

# Create your tests here.
class TweetTestCase(TestCase):

    def setup(self):

        # create tweets
        t1 = Tweet.objects.create(
            username='TestUser1',
            tip=f'This is a test tip from {username}',
            email='testuser1@test.com',
            )
        
        t2 = Tweet.objects.create(
            username='TestUser2',
            tip=f'This is a test tip from {username}',
            email='testuser2@test.com',
            )

        def test_t1(self):
            t1 = Tweet.objects.get(username='TestUser1')
            self.assertEqual(t1.email, 'testuser1@test.com')
            self.assertEqual(t1.username, 'TestUser1')            