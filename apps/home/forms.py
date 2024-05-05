from django import forms
from ckeditor.fields import CKEditorWidget
from .models import Evaluasi

class EvaluasiForm(forms.ModelForm):
    class Meta:
        model = Evaluasi
        fields = ['nama', 'grup', 'jawaban1', 'jawaban2', 'jawaban3', 'jawaban4', 'jawaban5', 'jawaban6']
        widgets = {
            'jawaban1': CKEditorWidget(),
            'jawaban2': CKEditorWidget(),
            'jawaban3': CKEditorWidget(),
            'jawaban4': CKEditorWidget(),
            'jawaban5': CKEditorWidget(),
            'jawaban6': CKEditorWidget(),
        }
