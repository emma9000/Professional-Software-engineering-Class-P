# Title 

## 🧩 Functional Requirements (FR)

| ID                                                 | Requirement                                                                             | Explanation                                                         | Current Status |
| -------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------- |
| **FR1 – User Registration and Login**              | Allow users to create accounts and sign in securely using JWT authentication.           | **In Progress** (backend under development by Emma)                 |                |
| **FR2 – User Data Separation (Multi-tenant)**      | Each user can access only their own transcripts, glossary, and summaries.               | **In Progress** (Emma implementing DB filtering & token validation) |                |
| **FR3 – Real-time Speech-to-Text (Transcription)** | Convert live or recorded English audio to text using Whisper API; display in real-time. | **Not Met** (to be implemented in Phase 1)                          |                |
| **FR4 – Transcript Storage**                       | Save full transcripts with timestamps and metadata to the database.                     | **Not Met** (schema ready but feature not yet connected)            |                |
| **FR5 – Dictionary / Word Meaning Panel**          | Enable users to select words, view definitions or translations, and add to glossary.    | **Not Met** (front-end UI planned by Dinasha)                       |                |
| **FR6 – Glossary Management (CRUD)**               | Let users view, add, and delete saved vocabulary with meanings.                         | **Not Met**                                                         |                |
| **FR7 – Auto Summarization**                       | Use GPT API to generate concise summaries of saved transcripts.                         | **Not Met** (planned for Phase 2)                                   |                |
| **FR8 – PDF Export**                               | Allow users to export transcripts, glossary, and summaries into formatted PDF files.    | **Not Met**                                                         |                |
| **FR9 – Error Handling & Notifications**           | Show loading indicators, error toasts, and retry options for failed API calls.          | **Not Met**                                                         |                |
| **FR10 – Rate Limiting & Audit Logs**              | Prevent API abuse and log essential events (login attempts, API usage).                 | **Not Met**                                                         |                |
| **FR11 – Role-based Access Control (Future)**      | Support role expansion (admin/user) for future scalability.                             | **Not Verified** (not required for current phase)                   |                |

---

## ⚙️ Non-Functional Requirements (NFR)

| ID                                              | Requirement                                                                    | Explanation                                    | Current Status |
| ----------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------- | -------------- |
| **NFR1 – Usability**                            | The interface should be intuitive; users can complete main tasks in ≤ 3 steps. | **Not Met** (UI prototype in progress)         |                |
| **NFR2 – Performance**                          | The system should display each transcription segment within 2–3 seconds.       | **Not Met** (pending real-time implementation) |                |
| **NFR3 – Reliability & Fault Tolerance**        | The app should recover gracefully from API failures and network errors.        | **Not Met**                                    |                |
| **NFR4 – Security**                             | Implement HTTPS, password hashing, and secure JWT tokens.                      | **In Progress** (Emma working on backend auth) |                |
| **NFR5 – Privacy & Data Protection**            | Users can delete their data; no exposure of sensitive information.             | **Not Met**                                    |                |
| **NFR6 – Maintainability**                      | Codebase structured with modular components, documented APIs, and linting.     | **In Progress**                                |                |
| **NFR7 – Deployability**                        | Frontend deployable to Vercel, backend to Render/Heroku, DB to Supabase.       | **Not Met**                                    |                |
| **NFR8 – Observability (Logging & Monitoring)** | Log requests, errors, and API usage for later analysis.                        | **Not Met**                                    |                |
| **NFR9 – Scalability**                          | Architecture supports future mobile or multilingual extensions.                | **Not Verified**                               |                |
| **NFR10 – Documentation & Tutorials**           | Provide README, API documentation, and setup guide.                            | **Not Met**                                    |                |
