from pathlib import Path
import win32com.client
import re
import datetime

def clean_subject(subject):
    # Remove invalid characters from the subject
    cleaned_subject = re.sub(r'[<>:"/\\|?*]', '', subject)
    return cleaned_subject.strip()  # Remove leading and trailing whitespaces

output_dir = Path.cwd() / "OUTPUT"
output_dir.mkdir(parents=True, exist_ok=True)

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Connect to the Inbox folder
inbox = outlook.GetDefaultFolder(6)

# Get today's date
today = datetime.datetime.now().date()

# Iterate through emails and filter for today only
for message in inbox.Items.Restrict("[ReceivedTime] >= '" + today.strftime('%m/%d/%Y 00:00 AM') + "'"):
    subject = message.Subject
    body = message.Body
    attachments = message.Attachments

    # Clean the subject to remove invalid characters and leading/trailing whitespaces
    cleaned_subject = clean_subject(subject)

    if "special order" in cleaned_subject.lower():
        target_subject = cleaned_subject

        target_folder = output_dir / target_subject
        target_folder.mkdir(parents=True, exist_ok=True)

        Path(target_folder / "EMAIL_BODY.txt").write_text(str(body))

        for attachment in attachments:
            attachment.SaveAsFile(target_folder / str(attachment))
