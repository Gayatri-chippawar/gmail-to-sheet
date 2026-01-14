from gmail_service import get_gmail_service, fetch_unread_emails
from email_parser import parse_email
from sheets_service import append_row
from config import SPREADSHEET_ID
from state_manager import load_state, save_state, is_processed, mark_processed
from gmail_service import get_gmail_service, fetch_unread_emails, mark_email_as_read


def main():
    service = get_gmail_service()
    state = load_state()

    messages = fetch_unread_emails(service)

    if not messages:
        print("No unread emails.")
        return

    for msg in messages:
        msg_id = msg["id"]

        # ✅ Skip duplicates
        if is_processed(msg_id, state):
            print(f"Skipping already processed email: {msg_id}")
            continue

        message = service.users().messages().get(
            userId="me",
            id=msg_id,
            format="full"
        ).execute()

        email_data = parse_email(message)

        append_row(
            SPREADSHEET_ID,
            [
                email_data["from"],
                email_data["subject"],
                email_data["date"],
                email_data["content"]
            ]
        )

        # ✅ Mark as processed
        mark_processed(msg_id, state)
        mark_email_as_read(service, msg_id)

        print(f"Processed & marked as read: {msg_id}")


    save_state(state)
    print("State saved successfully.")


if __name__ == "__main__":
    main()
