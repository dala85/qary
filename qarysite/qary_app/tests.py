from django.test import TestCase
from .models import Chat, Document


class BasicTest(TestCase):
    def test_fields(self):
        chat = Chat()
        chat.question = 'How are you?'
        chat.answer = "why you ask!"
        chat.save()

        record = Chat.objects.get(pk=1)
        self.assertEqual(record, chat)


if __name__ == '__main__':
    unittest.main()
