# 📄 Project Statement: Student Grading System

## 1. Problem Definition
Educational institutions often rely on manual methods or fragmented spreadsheet systems to track student academic performance. These traditional methods suffer from several critical issues:
*   **Human Error:** Manual calculation of weighted averages and GPAs is prone to mathematical mistakes.
*   **Inefficiency:** Teachers spend disproportionate amounts of time calculating grades rather than teaching.
*   **Data Redundancy:** Student records are often duplicated or lost across different physical files or non-centralized digital files.
*   **Delayed Feedback:** Students and parents often wait weeks for report cards to be manually compiled.

## 2. Proposed Solution
The **Student Grading System** is a centralized software solution designed to automate the academic evaluation process. It serves as a digital ledger for student information and a computational engine for academic metrics. By standardizing the grading logic, the system ensures fairness, accuracy, and efficiency in academic reporting.

## 3. Project Objectives
The primary objectives of this system are to:
1.  **Automate Calculation:** Eliminate manual computation of totals, percentages, and GPAs.
2.  **Centralize Data:** Store all student profiles and assessment records in a single, secure database.
3.  **Standardize Reporting:** Generate uniform, professional report cards and transcripts instantly.
4.  **Enhance Accessibility:** Allow quick retrieval of historical academic records for administrative decisions.

## 4. Scope of Work

### 4.1 In-Scope (Deliverables)
*   **User Authentication:** Login system for Administrators and Faculty.
*   **Database Management:** System to Add/Edit/Delete Student and Course records.
*   **Grade Processing:** Input interfaces for assignments, quizzes, and exams with auto-calculation of final grades.
*   **Ranking Logic:** Algorithms to determine class rank and distinction lists.
*   **Export Module:** Ability to generate PDF report cards and CSV summaries.

### 4.2 Out-of-Scope (Future Constraints)
*   **Online Payment Integration:** Fee collection is not part of this version.
*   **E-Learning Modules:** The system will not host video lectures or study materials.
*   **Parent Portal:** A separate interface for parents is reserved for Phase 2 development.

## 5. System Requirements

### 5.1 Functional Requirements
*   **FR-01:** The system must allow the user to define specific weightages for different assessment types (e.g., Exam = 50%, Quiz = 20%).
*   **FR-02:** The system must prevent the deletion of a student record if grade data exists (referential integrity).
*   **FR-03:** The system must flag failing grades (e.g., < 60%) automatically in generated reports.

### 5.2 Non-Functional Requirements
*   **Accuracy:** GPA calculations must be accurate to two decimal places.
*   **Performance:** Report generation for a class of 50 students must complete within 5 seconds.
*   **Security:** Student data must be stored locally with basic encryption or restricted access permissions.

## 6. Target Audience
*   **Primary Users:** Teachers, Professors, and Teaching Assistants.
*   **Secondary Users:** School Administrators and Registrars.
*   **Beneficiaries:** Students (receivers of accurate reports).

## 7. Success Metrics
The project will be deemed successful if:
*   Grade calculation time is reduced by at least 70% compared to manual methods.
*   The error rate in Final GPA calculation reaches 0%.
*   The system successfully manages a dataset of at least 500 active students without crashing.
