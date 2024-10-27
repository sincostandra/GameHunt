from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from review.models import Review
from search.models import Game
from django.contrib.auth import get_user_model
import uuid

class ReviewTests(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a game
        self.game = Game.objects.create(
            id=uuid.uuid4(),
            name='Test Game',
            year=2023,
            description='A test game description.',
            developer='Test Developer',
            genre='Action',
            ratings=4.5,
            harga=100,
            toko1='Test Store 1',
            alamat1='Test Address 1'
        )

        # Create a review
        self.review = Review.objects.create(
            game=self.game,
            user=self.user,
            title='Test Review',
            content='This is a test review content.',
            score=5
        )

    def test_show_reviews(self):
        response = self.client.get(reverse('review:show_reviews', args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Review')

    def test_create_review_ajax(self):
        response = self.client.post(reverse('review:create_review_ajax', args=[self.game.id]), {
            'title': 'New Review',
            'score': 4,
            'content': 'This is a new review.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Review')

    def test_vote_review(self):
        response = self.client.post(reverse('review:vote_review'), {
            'review_id': self.review.id,
            'vote_type': 'upvote'
        })
        self.assertEqual(response.status_code, 200)
        self.review.refresh_from_db()
        self.assertIn(self.user, self.review.upvotes.all())

        # Test downvote
        response = self.client.post(reverse('review:vote_review'), {
            'review_id': self.review.id,
            'vote_type': 'downvote'
        })
        self.assertEqual(response.status_code, 200)
        self.review.refresh_from_db()
        self.assertIn(self.user, self.review.downvotes.all())

    def test_remove_review_ajax(self):
        response = self.client.post(reverse('review:remove_ajax'), {
            'id': self.review.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())

    def test_get_user_review(self):
        response = self.client.get(reverse('review:get_user_review', args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Review')

    def test_get_review_json(self):
        response = self.client.get(reverse('review:get_review_json', args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [{
            'id': self.review.id, 
            'username': self.user.username,
            'title': self.review.title,
            'content': self.review.content,
            'score': self.review.score,
            'date': str(self.review.date)[:10] + " " + str(self.review.date)[11:20],
            'vote_score': self.review.vote_score,
            'user_upvoted': False,
            'user_downvoted': False
        }])

    def tearDown(self):
        self.user.delete()
        self.game.delete()
        self.review.delete()