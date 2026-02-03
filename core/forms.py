from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'bg-white/5 border border-white/10 text-[var(--text-main)] p-4 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500/50 transition-all placeholder:text-slate-600',
        'placeholder': 'John Doe'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'bg-white/5 border border-white/10 text-[var(--text-main)] p-4 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500/50 transition-all placeholder:text-slate-600',
        'placeholder': 'john@example.com'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'bg-white/5 border border-white/10 text-[var(--text-main)] p-4 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500/50 transition-all placeholder:text-slate-600',
        'placeholder': 'Project Inquiry'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'bg-white/5 border border-white/10 text-[var(--text-main)] p-4 w-full h-40 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500/50 transition-all placeholder:text-slate-600',
        'placeholder': 'How can I help you?'
    }))
