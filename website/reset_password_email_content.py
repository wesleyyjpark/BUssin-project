reset_password_email_html_content="""
<p>Hello</p>
<p>You are receiving this email because you requested a password reset for your account.</p>
<p>
    To reset your password
    <a href="{{ reset_password_url }}">click here</a>
</p>
<p>
    Alternatively, you can paste the following link in your browser's address bad: <br>
    {{ reset_password_url }}
</p>
<p>If you have not requested a password reset, be careful of sharing your email with others</p>
<p>
    Thank you!
</p>
"""