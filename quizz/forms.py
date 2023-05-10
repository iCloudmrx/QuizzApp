from django import forms
from .models import Question, Test


class TestForm(forms.Form):
    class Meta:
        model = Test
        fields = ['title', 'max_attemps',
                  'pass_percentage', 'start_date', 'end_date']

    def save(self, request, comment=True):
        test = self.instance
        test.author = request.user
        super().save(comment)
        return test.id


class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = '__all__'
    submit_and_exit = forms.BooleanField(required=False)

    def save(self, test_id, comment=True):
        question = self.instance
        question.test = Test.objects.get(id=test_id)
        super().save(comment)
        return question
