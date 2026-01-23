from django.test import TestCase
from django.urls import reverse

from memos.models import Memo


class MemoViewTests(TestCase):
    def test_list_page_ok(self):
        res = self.client.get(reverse("memo_list"))
        self.assertEqual(res.status_code, 200)

    def test_create_requires_title(self):
        res = self.client.post(reverse("create_memo"), data={"title": "", "body": "x", "tags": ""})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "タイトルは必須")

    def test_memo_detail_404_for_nonexistent_id(self):
        """Test that accessing a non-existent memo returns 404"""
        res = self.client.get(reverse("memo_detail", args=[99999]))
        self.assertEqual(res.status_code, 404)

    def test_edit_memo_404_for_nonexistent_id(self):
        """Test that editing a non-existent memo returns 404"""
        res = self.client.get(reverse("edit_memo", args=[99999]))
        self.assertEqual(res.status_code, 404)

    def test_memo_detail_ok_for_existing_id(self):
        """Test that accessing an existing memo returns 200"""
        memo = Memo.objects.create(title="Test Memo", body="Test body")
        res = self.client.get(reverse("memo_detail", args=[memo.id]))
        self.assertEqual(res.status_code, 200)

    def test_edit_memo_ok_for_existing_id(self):
        """Test that editing an existing memo returns 200"""
        memo = Memo.objects.create(title="Test Memo", body="Test body")
        res = self.client.get(reverse("edit_memo", args=[memo.id]))
        self.assertEqual(res.status_code, 200)

    # TODO: detail/edit/delete / legacy検索 / pagination のテストを追加
