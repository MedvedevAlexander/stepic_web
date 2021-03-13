from django import forms
from .models import Author, Book, Question, Answer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Временно сделано, нужно исправить:
# 1. В моделях поле Question.author, Answer.author разрешено сохранение пустого значения blank=True.
# Это необходимо убрать


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data, author=self._user)
        question.save()

        return question


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(max_length=100, required=False)

    def save(self, question):
        answer = Answer(text=self.cleaned_data['text'], question=question, author=self._user)
        answer.save()

        return answer


class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, initial='Оставьте здесь ваше сообщение')
    sender = forms.EmailField
    cc_myself = forms.BooleanField(required=False)
    birth_year = forms.DateField(widget=forms.SelectDateWidget)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name != 'Alexander':
            raise ValidationError('Имя указано неверно, укажите настоящее имя')
        return self.cleaned_data

    def clean(self):
        birth_date = self.cleaned_data['birth_date']
        if str(birth_date) != '1993-07-17':
            raise ValidationError('Дата рождения указана неверно')
        return self.cleaned_data


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) <= 8:
            raise ValidationError('Длина пароля должна быть как минимум 8 символов')

        return password

    def clean_email(self):
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except ObjectDoesNotExist:
            pass
        else:
            raise ValidationError('Данный email уже используется')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']