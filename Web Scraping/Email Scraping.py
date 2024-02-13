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

excel_attachments_dir = output_dir / "Excel Attachments"
excel_attachments_dir.mkdir(parents=True, exist_ok=True)

other_attachments_dir = output_dir / "Other Attachments"
other_attachments_dir.mkdir(parents=True, exist_ok=True)

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Connect to the Inbox folder
inbox = outlook.GetDefaultFolder(6)

# Get today's date
today = datetime.datetime.now().date()

yesterday = today - datetime.timedelta(days=1)

# Iterate through emails and filter for yesterday only
for index, message in enumerate(inbox.Items.Restrict("[ReceivedTime] >= '" + yesterday.strftime('%m/%d/%Y 00:00 AM') + "'")):
    subject = message.Subject
    sender_name = message.SenderName
    body = message.Body
    attachments = message.Attachments

    # Clean the subject to remove invalid characters and leading/trailing whitespaces
    cleaned_subject = clean_subject(subject)

    if "special order" in cleaned_subject.lower():
        target_subject = f"{index + 1}_{sender_name}"  # Include index in folder name

        target_folder = excel_attachments_dir if any(attachment.FileName.endswith(".xlsx") for attachment in attachments) else other_attachments_dir
        target_folder = target_folder / target_subject
        target_folder.mkdir(parents=True, exist_ok=True)

        # Save email body if needed
        # Path(target_folder / "EMAIL_BODY.txt").write_text(str(body))

        for attachment in attachments:
            # Exclude PNG files
            if not attachment.FileName.endswith((".png", ".jpg")):
                attachment.SaveAsFile(target_folder / str(attachment))
