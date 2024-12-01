import wikipedia

def main():
    print("Wikipedia Search")
    while True:
        search_term = input("Enter page title or search phrase (blank to quit): ")
        if not search_term.strip():
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_term, autosuggest=True)
            print_page_details(page)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def print_page_details(page):
    """Print details of the Wikipedia page."""
    print(f"\nTitle: {page.title}")
    print(f"Summary: {page.summary[:500]}...")  # Truncate summary for readability
    print(f"URL: {page.url}\n")


if __name__ == "__main__":
    main()