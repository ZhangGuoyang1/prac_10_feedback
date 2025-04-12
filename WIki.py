
import wikipedia


def search_wikipedia():
    """
    Prompt the user to enter the Wikipedia page title until the input is empty.
    """
    user_input = input("Enter page title (or press Enter to quit): ").strip()
    while user_input != "":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"\nTitle: {page.title}\n")
            summary = wikipedia.summary(user_input, sentences=3)
            print(f"Summary: {summary}\n")
            print(f"URL: {page.url}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')
        except Exception as ex:
            print("An error occurred:", ex)

        user_input = input("\nEnter another page title (or press Enter to quit): ").strip()

    print("Thank you.")


if __name__ == "__main__":
    search_wikipedia()
