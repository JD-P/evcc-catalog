from django import forms
class SimpleSearchForm(forms.Form):
    multisearch = forms.CharField(max_length=5096)
    
    monday = forms.BooleanField(label="Monday", required=False)
    tuesday = forms.BooleanField(label="Tuesday", required=False)
    wednesday = forms.BooleanField(label="Wednesday", required=False)
    thursday = forms.BooleanField(label="Thursday", required=False)
    friday = forms.BooleanField(label="Friday", required=False)

    annual = forms.BooleanField(label="Annual Course", required=False)
    ec = forms.BooleanField(label="Taught At East SnoCo Location",
                            required=False)
    hybrid = forms.BooleanField(label="Hybrid Course", required=False)
    honors = forms.BooleanField(label="Honors Course", required=False)
    lc = forms.BooleanField(label="Learning Community", required=False)
    online = forms.BooleanField(label="Online Course", required=False)
    web_enhanced = forms.BooleanField(label="Web Enhanced", required=False)
    
    aas = forms.BooleanField(label="Satisfies Option II code",
                             required=False)
    c = forms.BooleanField(label="Satisfies Communication Skills Requirement",
                           required=False)
    ns = forms.BooleanField(label="Satisfies Natural Science Requirement",
                            required=False)
    h = forms.BooleanField(label="Satisfies Humanities Requirement",
                           required=False)
    hp = forms.BooleanField(label="Satisfies Humanities Performance Requirement",
                            required=False)
    ss = forms.BooleanField(label="Satisfies Social Sciences Requirement",
                            required=False)
    ns_l = forms.BooleanField(label="Satisfies Natural Science Lab Requirement",
                              required=False)
    q = forms.BooleanField(label="Satisfies Quantitative Skills Requirement",
                           required=False)
    te = forms.BooleanField(label="Satisfies Transfer Elective Requirement",
                            required=False)
    d = forms.BooleanField(label="Satisfies Diversity Course Requirement",
                           required=False)
