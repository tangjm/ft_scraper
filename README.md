# Scraper for the Financial Times

Sample article link html structure

```html 
<a
data-trackable="heading-link"
data-trackable-context-story-link="heading-link"
href="/content/2a23cc70-3c3a-4e18-9020-a9bab70b07a3"
class="link"
target="\_self"
aria-describedby=""

> <span
    placeholder="headlineIndicator"
    class="headline-indicator"
    ><span
      class="icon icon--opinion icon--scale-3"
    >
      <span
        class="o-normalise-visually-hidden"
        >opinion content. </span
      ></span
    ><span
      class="text text--color-black text-display--scale-3 text--weight-600"
      id=""
      >The FT View.
    </span></span
> <span
    class="text text--color-black text-display--scale-3 text--weight-500"
    id=""
    >Tough economic realities await
    Britain’s next leader</span
> </a
```

Features
- [x] Grab all main stories that have the attribute `data-trackable-context-story-link="heading-link"`
- [x] Also extract titles and links to main stories 
- [ ] Make a request to the website using the urllib library
