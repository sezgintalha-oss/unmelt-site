# Privacy Policy

Version 1.0 — Last updated 2026-11-25

## 1. Who we are and what this policy covers

Unmelt (the "app") is operated by Mamonta Dış Ticaret A.Ş. ("we", "us"), a
company registered in Türkiye. Address: Akyapi D:49, No:23, Ikitelli OSB Mahallesi, Bedrettin Dalan Bulvari, 34490 Basaksehir, Istanbul, Türkiye. Email:
privacy@mamonta.com. We are responsible for the personal information described
in this policy.

Unmelt is an app for parents and legal guardians. It offers a library of
narrated, animated picture-book stories about everyday feelings, and lets you
create a story for your child with the help of AI. This policy explains what
information the app collects, why, who receives it, how long we keep it and
what your rights are.

## 2. Information we collect

- Account: your email address, your display name (the name your Apple or
  Google account shares, otherwise the part of your email before "@"), your
  password if you sign up with email (stored only as a hash by our
  authentication provider) and an internal user ID.
- Guest session: you can try the app before creating an account. This creates
  an internal user ID with no email. Guest sessions cannot buy subscriptions.
- Your acceptance of the Terms of Use and this Policy (which document, which
  version, when).
- Child profile: your child's first name or nickname, birth year and,
  optionally, birth month (we never ask for the day), gender (girl, boy or
  "prefer not to say"), an avatar picked from a built-in set and, if you
  choose it, a simpler reading level preference. When you try the app as a
  guest, your child's name is optional and an approximate birth year is derived
  from the age you pick; if you leave it blank, the app uses a general name
  ("Your child"). A child profile you create in an account requires a name.
  When the option to order for another child without creating a profile is
  enabled, that child's first name and gender are stored only on that book
  record and are deleted after 90 days together with your order answers (see
  section 7).
- Personal books you order: your answers to the order questions about your
  child's situation (see section 2.1), the change requests you send about a
  draft, and the book made from them (its title, text, hero name and drawing,
  pictures, animations, narration, music and, in versions of the app that
  offer them, PDF files). If a book's text or
  hero name is edited, earlier versions are kept (see section 7).
- Library use: which library stories you opened in each free or subscription
  period, the page you last reached, stories you marked as favourites, your
  narrator and background-sound choice, stories or authors you hid, and content
  reports you send (story, page, reason and an optional note).
- Reading days: we store the dates on which a child profile reached the end of
  a story, to show a reading streak. This version of the app does not ask your
  child any question and does not collect feelings answers. If answers were
  given in an earlier version of the app (a face for "good", "so-so" or "not
  good" at the end of a library story), they stay stored with the child profile
  in your account until you delete the child profile or your account.
- Reading and listening events: to show a child's monthly calendar and the
  month's favourites on the Reading summary screen, we store the local day on
  which a child profile reached the end of a story or listened to a story on
  Story Radio, the timestamp when the record was created, and which story it
  was; the story's content is not stored in this record. On Story Radio we also
  store when each child profile last listened to each radio story (so stories
  are not repeated back to back) and, to enforce the rolling 24-hour free
  listening allowance, when your account opened a radio story and the seconds
  counted toward that allowance (see section 7).
- Subscription and credits: whether your subscription is active, when the
  current period ends, the product, whether you are in a free trial, store
  purchase events, and the history of book credits added, used and returned.
  We never receive your card or bank details.
- Books you publish or share: see section 2.3.
- Notifications: if you allow notifications, a device push token and the
  platform (iOS or Android), used to tell you when a draft or a book is ready.
- Error reports: see section 2.2.

We do not collect your location, advertising ID or photos, and we do not use
advertising or analytics SDKs. We do not collect health data from your device
(such as Apple Health or step counts); the "sensitive information" described
below is only the text you write yourself.

### 2.1 Sensitive information: the text you write about your child

When you create a story, you can describe your child's situation in your own
words. This is free text. It may, even unintentionally, include information
about health, a disability, beliefs or other sensitive matters. We therefore
treat this text as sensitive personal information, whatever you write:

- We use it only to write your child's story. We never use it for
  advertising, profiling or training AI models, and we never show it to anyone
  other than you.
- The text is sent to Anthropic, the AI provider that writes the story (see
  section 5).
- We delete the raw text within 90 days at the latest (see section 7). You can ask us to delete it sooner (see section 8).
- Writing this text is optional for using the app: you can read library
  stories without it. A personal book cannot be ordered without it, because
  the order questions need written answers.
- We ask for your explicit consent before you can write this text. Before
  your first order is sent, the app shows a notice that summarises the points
  above, with a consent box that is not pre-ticked. Until you consent to the
  current notice version, an order or change request cannot be sent; our server
  checks this on active order and revision endpoints and rejects the request
  without storing the text if consent is missing. If you do not consent, you
  can keep using the library. You can withdraw your consent at any time from the Profile screen (see section 3).
- As a safety net on legacy server endpoints, if text is ever processed without
  that consent step (for example, a direct call to a legacy endpoint outside
  the app), we record the event in an audit log: your user ID, the hour it
  happened, the consent state ("never given" or "withdrawn") and a size band of
  the text (short, medium or long). The text itself, any part of it, a summary
  of it or an encrypted trace of it is never written to that log. We keep this
  log only to check that the consent step works and, if needed, to notify you.
  It is deleted automatically after 180 days (see section 7).

### 2.2 Error reports (Sentry)

When the app hits an error, it sends an error report to Sentry, our error
monitoring provider. We build each report ourselves, and a filter in the app
removes everything except these fields: an error code, the error type, where
the error came from in the app, the name of the screen, the app version and
build number, and the time.

Error reports do not include your user ID, email, name, your child's
information, the text you write, story content, screen text, device details
or a record of what you tapped. Automatic crash, hang and session tracking
are switched off. When a report arrives, Sentry's servers see the network
address of the connection, as any internet service does; the app does not
send it as part of the report.

Our servers also send error reports to Sentry when story creation fails.
These reports contain a short error summary chosen from a fixed list, the
error type, where the error came from and technical details of our own code.
They do not include your user ID, email, your child's information, the text
you write or story content.

### 2.3 Books you publish or share

This feature is not available in this version of the app. If we add it in a later version, it will work as described below and only when you ask for it.

Two features show a personal book to people other than you. Both work only
when you ask for them.

- Sending a book to the library: before publication, an automatic check reads
  the book's title, page text and hero name, and our team reviews the whole
  book, including its pictures and narration. Names the check finds are
  stored with your request during the review and deleted when the request is
  closed. If the book is published, a copy is shown to other users of the
  app: its title, page text, pictures or animations, narration, music,
  language and age band. The copy does not include the cover text, your
  answers to the order questions or your change requests. We do not show your
  name or email with the book. Names in the story, including your child's
  name, are not removed. We keep a record of each request and of the review
  decisions (what was decided and when).
- Sharing a book by link: we create a link for the book. The book can then be
  read by anyone who opens the link in the app, signed in or in a guest
  session: its title, cover, cover text, pages, pictures, narration and music,
  including your child's name if it appears in the book. We record which
  accounts opened the link, so that the book appears in their My Books, and
  we record attempts to create or open links, to limit misuse. We do not show
  your name or email with the shared book, and the app does not show you who
  opened the link.

## 3. Legal bases (Türkiye, EU and UK)

Where the law requires a legal basis for processing personal information (for
example the Turkish data protection law, KVKK, and the EU or UK GDPR):

- Account, stories, library, subscription and credits: performance of our
  contract with you (KVKK Art. 5(2)(c), GDPR Art. 6(1)(b)).
- Your child's profile (name, birth month and year, gender): performance of
  our contract with you, because a story suited to your child cannot be made
  without it (KVKK Art. 5(2)(c), GDPR Art. 6(1)(b)). We do not ask for a
  separate consent for this data; section 2 lists what we process and you can
  use your rights in section 8 at any time.
- The text you write about your child: your explicit consent (KVKK Art. 5(1) and KVKK Art. 6(2), GDPR Art. 6(1)(a) and GDPR Art. 9(2)(a)).
  Because we treat this text as sensitive, the basis is your explicit consent,
  not the contract. We record who gave consent, when, and for which version
  of this notice. Writing the text is optional: without consent you can
  still read the library, but a personal book cannot be ordered.
- You can withdraw your consent at any time (Profile → Sensitive data consent; KVKK Art. 11, GDPR Art. 7(3)).
  Withdrawal applies from that moment on: stories already made, their text
  and pictures stay; the app only stops accepting new free text. Raw text
  already given is still deleted under section 7, and you can ask for earlier
  deletion under section 8.
- Publishing a book to the library and sharing a book by link: performance
  of our contract with you, because you ask for it (KVKK Art. 5(2)(c), GDPR
  Art. 6(1)(b)). Reviewing books before publication and handling reports: our
  legitimate interest in keeping the library safe for children.
- Error reports and security measures: our legitimate interest in keeping
  the app secure and working.
- Push notifications: the notification permission you give on your device.
- Records we must keep by law (for example purchase records): legal
  obligation.

## 4. Why we use information

- To create your child's story text, pictures, page animations, narration,
  background music and, when you ask for one, a print-ready PDF file. PDF files are not available in this version of the app.
- To run the story library, Story Radio, reading progress, favourites and reading streak
- To tell you that a draft or a book is ready (push notification and in-app notification history)
- To publish books you send to the library, after review, and to share books
  you choose by link
- To manage your account, subscription and book credits
- To keep the app secure and working, including error reports

We do not use your information for advertising and we do not sell it.

## 5. Who receives information

Service providers process information for us, only as far as they need it.
Other people receive information only when you publish or share a book:

- Supabase, Inc. — authentication, database, file storage and server
  functions. Holds all account, child-profile, story and usage data. Our
  project is hosted in the United States (AWS us-east-1).
- Anthropic, PBC — writes the story text, scene prompts and narration direction
  with AI, and checks generated frames for quality. Receives your answers to
  the order questions, the change requests you send, your child's first name,
  gender and age band, draft page text and hero names you edited, and generated
  character, page and video frames.
- Google (Google Flow) — draws the hero, pictures and animations of a
  personal book with AI. Receives picture and animation instructions written
  from the book's story (descriptions of scenes and characters) together with
  generated character reference sheets, style anchors and page images for
  visual consistency; it does not receive your raw answers to the order
  questions.
- Google (Google Gemini) — runs automated visual quality checks on generated
  page pictures (including hero drawings). Receives generated page images and a
  technical inspection prompt; it does not receive your answers to the order
  questions.
- QuickDesign (and video upscaling sub-processor ByteDance) — draws story
  pictures with AI and, for animated books, upscales generated silent 720p
  story video clips using the ByteDance video upscaling model. Receives scene
  descriptions made from the story and generated silent 720p story video clips,
  not the text you wrote or the narration audio.
- ElevenLabs, Inc. — reads a personal book aloud and makes its music with AI.
  Receives the book's title and page text (including phonetic pronunciation
  hints for your child's or hero's name and expression tags) for narration, and
  an instrumental music description for background music; it does not receive
  your answers to the order questions.
- OpenAI, L.L.C. — search by meaning in My Books. Receives the phrase you
  search for, the titles and topic tags of your books, and the titles,
  summaries and topic tags of library stories, and turns them into numbers
  used to compare meaning. Children's names are removed from the text before it is sent; a name that is
  shortened, inflected or written in an unusual way (for example, inside
  another word) may not be caught. This covers current and earlier child-profile
  names and the hero names of your books. Your notes about your child, your answers to the order
  questions and the story text do not go to OpenAI.
- Cloudflare, Inc. — serves our legal pages and, when link sharing is enabled,
  the web redirect bridge (`link.mamonta.com`) for shared book links. When a
  web page or share link is opened in a browser, Cloudflare processes standard
  HTTP connection data (IP address, browser User-Agent and requested URL path);
  it does not host story content.
- RevenueCat, Inc. — subscription status and purchase events. Identifies you
  by our internal user ID, not by your name or email.
- Apple (App Store) and Google (Google Play) — sell and bill subscriptions and
  handle refunds under their own privacy policies.
- Apple (Sign in with Apple) and Google (Google Sign-In) — only if you choose
  to sign in with them.
- Apple Push Notification service and Google Firebase Cloud Messaging —
  deliver push notifications. They receive the device token and the
  notification text. A notification about a book also carries the book's
  internal ID.
- Functional Software, Inc. (Sentry) — error reports, with only the fields in
  section 2.2. Our Sentry organisation is in the United States data region.
- Resend — sends sign-in and verification emails. Receives your email address
  and the email content.
- Other users of the app — only if you send a book to the library and it is
  published: they see the copy described in section 2.3.
- People you share a book with — only if you share a book by link: anyone
  who opens the link reads the book as described in section 2.3.

We may also disclose information if the law requires it, to protect rights and
safety, or as part of a sale or merger of our business, in which case the
buyer must follow this policy.

## 6. International transfers

We are based in Türkiye. Our database and files are stored in the United
States, and most of our service providers are in the United States. During the
video resolution upscaling step for animated books (run through QuickDesign's
ByteDance model), generated silent story video clips may also be processed on
servers outside the United States; no account identifier, audio narration or
order answers are sent in that step. Your information is therefore stored and
processed abroad as described above and may be accessed from Türkiye by our
staff for support and operations.

## 7. How long we keep data

Most of your information is kept until you delete your account. Several types
of data are deleted automatically after set periods:

- Your answers to the order questions and your change requests (and, when an
  order is placed without creating a child profile, the child name and gender
  on that book record) are deleted automatically 90 days after the last text
  step for that book finished (writing the first draft, or answering a change
  request); if no text step ever finished, the period starts when the order was
  placed. Approving the draft or making the finished book's pages, narration
  and music does not restart the clock. The same rule applies whether the book
  is finished, closed or cancelled. The only exception is a production step
  that is waiting in line or running at that moment: because that step may need
  your answers, they stay until it finishes. Only your answers and change
  requests are deleted; your book and its pictures stay.
- Account information, child profiles, stories, pictures, narration and
  animations: until you delete them or delete your account.
- Print-ready PDF files: PDF files are not available in this version of the app. If we add them in a later version: a PDF file generated on your request is deleted
  automatically from our file storage 30 days after it is created or last
  downloaded; you can generate it again in the app whenever you want while your
  book exists. The PDF request record is deleted with your book or your
  account.
- Earlier versions of a story's text and hero name you edited: only the last 20
  edits for each story are kept; older ones are deleted automatically. They are
  deleted at once if an order is cancelled, fails or closes unapproved after 14
  days, and otherwise with the story or your account, and only you can see
  them.
- Reading days, and any feelings answers given in an earlier version of the
  app: kept on our servers linked to the child profile. They are deleted when
  you delete the child profile or your account.
- Reading and listening events (the Reading summary calendar): kept on our
  servers linked to the child profile and deleted automatically after 24
  months. They are deleted at once when you delete the child profile or your
  account.
- Story Radio listening history and allowance records: when each child profile
  last listened to each radio story is kept until you delete the child profile
  or your account. Opening timestamps and counted seconds used to enforce the
  rolling 24-hour free Story Radio allowance are deleted automatically after 7
  days, and at once when you delete your account.
- Earlier names of a child profile: when you change a child's name or a book's
  hero name (or delete a child profile while non-cancelled stories remain on
  your account), the old name is kept so that search can still remove it from
  book titles before they are sent to OpenAI (section 5). If no non-cancelled
  stories remain on your account, a deleted child profile's name is not kept.
  It is used for nothing else, you cannot see it in the app, and it is deleted
  when you delete your account.
- Subscription status and the story-credit history: until you delete your
  account.
- Store purchase event log (event ID, event type, time and internal user ID):
  kept after you delete your account, for accounting, refund and fraud
  handling. When you delete your account, your internal user ID is removed
  from this log; the event ID, event type and time stay.
- Push token and in-app notifications: your push token is kept until you delete
  your account or turn off notifications on your device. In-app notification
  records are deleted after 60 days (when you open the notification panel) or
  when you clear them or delete your account.
- A book you sent to the library: the request and the review decisions are
  kept until you delete the book or your account. If you withdraw the book or
  it is taken down, it is no longer shown and its pictures and sound are
  deleted from the library storage; its text stays hidden with the request.
  When you delete the book or your account, the request and the library copy
  and its text are deleted. The log of review actions, admin audit and
  notification actions, and content reports (reason and optional note) that
  others sent about a published copy are kept for our records; they are no
  longer linked to the copy or to your account. If we stop an account from
  sending books to the library, that mark is kept until the account is deleted.
- Share links and the list of people who opened them: kept until you cancel
  sharing, delete the book or delete your account. When you cancel, the list
  of people is deleted; the cancelled link stays unusable until you delete the
  book or your account. Records of attempts to create or open links are kept
  until you delete your account. If someone who opened your link deletes
  their account, they are removed from the list.
- The audit log of text processed without consent (user ID, hour, consent
  state, size band; not the text): kept as a legacy-endpoint safety net and
  deleted automatically after 180 days. This is longer than the 90 days for the
  text on purpose, so that we can still check the consent step after the text
  is gone. You cannot see this log in the app; we will tell you about it if you
  ask under section 8.
- Error reports: kept by Sentry under the retention settings of our Sentry
  account. They contain no information that identifies you (section 2.2).
- A draft you do not approve within 14 days: the order is closed, the draft's
  title, text, edit history, hero name and hero drawing are removed from your
  library, and your book credit is not returned. Your answers are deleted under
  the 90-day rule above.
- An order form you have not sent: while you fill it in, the app keeps your
  answers and the order chat only on your device, in its encrypted storage, so
  they are not lost if the app closes, for example during payment. This copy
  is not sent to our servers before you place the order. It is deleted after
  24 hours, when you place the order, when you sign out or when you delete your
  account. If you cancel a book you ordered, the choices you made for it stay
  in the same encrypted storage for up to 14 days so you can start again with
  the same choices; they are deleted earlier when the book is ready, when you
  sign out or when you delete your account.
- Reading counters on your device (the dates you read, for up to the last
  400 reading days, and the highest page reached in each story): kept only on
  your device and never sent to our servers. They are deleted when you sign
  out or delete your account. The calendar and favourites on the Reading
  summary screen come from the reading and listening events above, not from
  these counters.

Information kept only on your device may be included in your own device
backups (for example iCloud or Google backups). Those backups are in your own
account and we cannot access them.

When the raw text is deleted, it is replaced with a deletion marker. After that,
in-app search finds the story only by its title, not by the words you wrote.
If the story has no title yet, search does not show it, but the story stays
in your library.

When you delete your account, your information is deleted immediately from
our database, except the de-identified store purchase event log and the
review/moderation records described above and records we must keep by law. Your
story pictures, narration, videos and PDF files are removed from our file
storage shortly after. Encrypted backups of our database and file storage are
kept for up to 30 days and then deleted; we also keep a non-identifying
encrypted deletion tombstone (HMAC) for 60 days so that a deleted account
cannot be restored if a backup ever has to be replayed. Your subscription
record held by RevenueCat and the stores is kept under their own rules. We do
not delete accounts because they are inactive; deleting your account is your
decision.

## 8. Your rights

Depending on where you live (including under US state privacy laws, KVKK
Art. 11 and GDPR Art. 15–21), you may have the right to:

- know what personal information we hold about you and get a copy of it
- correct inaccurate information
- delete your information
- restrict or object to processing
- withdraw consent at any time
- not be treated differently for using these rights

We do not sell or share personal information for targeted advertising and we
do not make automated decisions that have legal or similar effects on you.

In the app you can edit or delete child profiles and delete your account
(Profile → Delete my account). Deleting your account does not cancel a
subscription bought through Apple or Google; cancel it in your store account
settings. For a copy of your data, early deletion of the text you wrote, or
any other request, email privacy@mamonta.com from the email address on your
account. You can also complain to your data protection authority or, in the
US, your state attorney general.

## 9. Children's information

The account holder must be an adult parent or legal guardian. Accounts are meant to be created by a parent or guardian. The stories are made for children, so the library, the
reader, Story Radio and My Books may be used by a child on your device. This
section is our notice about children's information. The operator is Mamonta
Dış Ticaret A.Ş.; its address and email are in section 13.

Parental consent: a child profile can only be added after the parental
check is passed and you give your explicit consent for that profile. We keep
your consent together with the version of the consent text and the time it
was given, and for each child profile we keep a record of the consent it was
created under. If you withdraw your consent, no new child profile can be
added; existing profiles stay until you delete them.

Age signal: if your device supports it and age range sharing is allowed, the
app reads your device's age signal (Apple's age range sharing or Google Play
age signals). If the signal reports that the account belongs to someone under
18, purchases and account actions are routed to a parent. The signal is only
read on the device; it is not sent to our servers or stored. If there is no
signal, the parental check works as usual.

Our child safety rules (our stance against child sexual abuse material and
our reporting obligations) are in the Child Safety Policy in the app.

What we collect about a child, and how:

- Information you enter: your child's name or nickname, birth month and year,
  gender, avatar and the text you write about your child (sections 2 and
  2.1). We ask for the birth month and year, not the full date, because that
  is what we need to choose stories for your child's age. We treat the text
  you write as sensitive: we use it only to make the story and we delete the raw version within 90 days at the latest (see sections 2.1 and 7).
- Information recorded while the app is used, which can happen while a child
  is holding the device: which library stories were opened, the page last
  reached, favourites, narrator and background-sound choices, reading days
  and the other reading and listening records described in section 2, the
  words typed into search (section 5; search words are not stored) and
  content reports, including their optional note. These records are linked to your account and, where section
  2 says so, to a child profile. We use them only to run the app, for
  example to continue a story, show reading days, make search work and review
  reports.
- Technical data needed to run the service: an internal user ID, a push
  token if you allow notifications, and error reports reduced to the fields
  in section 2.2.

We do not show ads, we do not use advertising or analytics SDKs, and we do
not collect a child's advertising ID, location, photos or voice. Publishing
and sharing a book are behind a parent check in the app and are meant for
the account holder; a book sent to the library is published only after our
team reviews it (section 2.3). If a book is published or shared, your
child's name may appear in it and other people can read it.

The service providers listed in section 5 process this information for us,
only for the purposes described there. We do not sell children's information
and we do not disclose it to third parties for their own purposes, except as section 5 describes. How long
each type is kept is in section 7.

As a parent you can review the information we hold about your child, have it
deleted, and refuse further collection or use of it. In the app you can edit
or delete a child profile and delete your account (section 8). For a copy,
for deletion or to stop further collection, email privacy@mamonta.com from the
email address on your account. The app has no setting to stop these records
while it is used: deleting the account stops all of them, and deleting a
child profile stops those linked to that profile. We will tell you what each
step removes.

If you believe a child has given us information without a parent, email
privacy@mamonta.com and we will delete it.

## 10. AI-generated content

The stories, pictures and narration in the app are created with generative
AI. The text and pictures you see were made by AI models, not written or
drawn by a person. We state this in line with Art. 50 of the EU AI Act.

## 11. Security

Each account can read only its own data, except books you publish or share
(section 2.3) and books under review, which our team can read; this is
enforced in the database.
Connections are encrypted (HTTPS). Passwords are stored only as hashes by our
authentication provider. Error reports are reduced to a fixed list of fields
before they are sent. If a security breach affects your information, we will
notify you and the authorities as the law requires.

## 12. Changes to this policy

If we change this policy in a way that matters (for example a new type of
data, a new recipient or a longer retention period), we will show the new
version in the app and ask you to accept it before you continue. The version
and date are at the top of this page.

## 13. Contact

Mamonta Dış Ticaret A.Ş.
Akyapi D:49, No:23, Ikitelli OSB Mahallesi, Bedrettin Dalan Bulvari, 34490 Basaksehir, Istanbul, Türkiye
Email: privacy@mamonta.com
