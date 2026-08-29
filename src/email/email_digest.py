import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.articale_web_scraping.articale_web_scraping import ArticaleScraping

from dotenv import load_dotenv


class EmailDigest:
    def __init__(self):
        pass

    def send_lateat_5_articales_on(self, topic):
        articale_scraping = ArticaleScraping()
        get_5_articales = articale_scraping.get_the_5_latest_articale_on(topic)

        load_dotenv()

        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")

        # 2. Build the email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Guardian Tech News Digest"
        message["From"] = sender_email
        message["To"] = receiver_email

        html_header = """  <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Tech Headlines</title>
        </head>
        <body style="margin: 0; padding: 0; background-color: #f4f6f8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1a1a1a;">
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #f4f6f8; padding: 20px 0;">
            <tr>
              <td align="center">
                <!-- Main Card Container -->
                <table role="presentation" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); border: 1px solid #e5e7eb;" cellspacing="0" cellpadding="0" border="0">
                  
                  <!-- Header -->
                  <tr>
                    <td style="background-color: #052962; padding: 24px 30px;">
                      <h2 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 700; letter-spacing: -0.5px;">
                        ⚡ The 5 latest AI articales
                      </h2>
                    </h2>
                  </tr> 
                  
                  <!-- Content Body -->
                  <tr>
                    <td style="padding: 30px;">
                      <p style="margin-top: 0; margin-bottom: 20px; font-size: 15px; color: #4b5563; line-height: 1.5;">
                        Here are the latest updates from the technology sector:
                      </p>
        
                      <!-- Articles List -->
                      <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                      """

        html_body = """ """
        for title, link in get_5_articales.items():
            html_body += f""" <tr>
                                    <td style="padding: 16px 0; border-bottom: 1px solid #f3f4f6;">
                                      <a href="{link}" style="font-size: 16px; font-weight: 600; color: #052962; text-decoration: none; display: block; line-height: 1.4;">
                                        {title}
                                      </a>
                                      <span style="font-size: 13px; color: #6b7280; margin-top: 4px; display: block;">The Guardian • Tech</span>
                                    </td>
                                  </tr> """

        html_footer = """
                      </table>
                    </td>
                  </tr>
        
                  <!-- Footer -->
                  <tr>
                    <td style="background-color: #f9fafb; padding: 20px 30px; text-align: center; border-top: 1px solid #e5e7eb;">
                      <p style="margin: 0; font-size: 12px; color: #9ca3af;">
                        Automated Tech Digest • Generated via The Guardian API
                      </p>
                    </td>
                  </tr>
        
                </table>
              </td>
            </tr>
          </table>
        </body>
        </html> """

        html_content = html_header + html_body + html_footer

        # Attach content
        part = MIMEText(html_content, "html")
        message.attach(part)

        # 3. Connect to the SMTP Server & Send
        smtp_server = "smtp.gmail.com"
        port = 465  # Standard port for SSL

        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_test(self):
        # 1. Load configuration
        load_dotenv()

        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")

        # 2. Build the email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Guardian Tech News Digest"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Construct HTML content (insert your scraped Guardian articles here)
        html_content = """
        <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tech Headlines</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f6f8; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1a1a1a;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #f4f6f8; padding: 20px 0;">
    <tr>
      <td align="center">
        <!-- Main Card Container -->
        <table role="presentation" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); border: 1px solid #e5e7eb;" cellspacing="0" cellpadding="0" border="0">
          
          <!-- Header -->
          <tr>
            <td style="background-color: #052962; padding: 24px 30px;">
              <h2 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 700; letter-spacing: -0.5px;">
                ⚡ Top Tech Headlines Today
              </h2>
            </h2>
          </tr>

          <!-- Content Body -->
          <tr>
            <td style="padding: 30px;">
              <p style="margin-top: 0; margin-bottom: 20px; font-size: 15px; color: #4b5563; line-height: 1.5;">
                Here are the latest updates from the technology sector:
              </p>

              <!-- Articles List -->
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                <!-- Article 1 -->
                <tr>
                  <td style="padding: 16px 0; border-bottom: 1px solid #f3f4f6;">
                    <a href="https://www.theguardian.com/technology" style="font-size: 16px; font-weight: 600; color: #052962; text-decoration: none; display: block; line-height: 1.4;">
                      Sample Guardian Article 1
                    </a>
                    <span style="font-size: 13px; color: #6b7280; margin-top: 4px; display: block;">The Guardian • Tech</span>
                  </td>
                </tr>

                <!-- Article 2 -->
                <tr>
                  <td style="padding: 16px 0;">
                    <a href="https://www.theguardian.com/technology" style="font-size: 16px; font-weight: 600; color: #052962; text-decoration: none; display: block; line-height: 1.4;">
                      Sample Guardian Article 2
                    </a>
                    <span style="font-size: 13px; color: #6b7280; margin-top: 4px; display: block;">The Guardian • Tech</span>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color: #f9fafb; padding: 20px 30px; text-align: center; border-top: 1px solid #e5e7eb;">
              <p style="margin: 0; font-size: 12px; color: #9ca3af;">
                Automated Tech Digest • Generated via The Guardian API
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
        """

        # Attach content
        part = MIMEText(html_content, "html")
        message.attach(part)

        # 3. Connect to the SMTP Server & Send
        smtp_server = "smtp.gmail.com"
        port = 465  # Standard port for SSL

        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
