# All-in-one-resumeOperations
ML-Based CV Recommender and Generator
Version 1.0

Project Team:

Supervisor: Obad Zafar
Team Leader: Syed Shahzain Hassan
Team Members: Abdul Moiz Abid, Sufyan Siddiqui, Muhammad Sameed Fayiz, Muhammad Ammar
Date: September 09, 2023

Table of Contents
Introduction
1.1. Purpose
1.2. Intended Audience and Reading Suggestions
1.3. Project Scope
Overall Description
2.1. Product Perspective
2.2. Product Features
2.3. User Classes and Characteristics
2.4. Operating Environment
System Features
3.1. Parsing
3.2. Keywords Extraction
3.3. Vector Similarity
3.4. CV Matcher
3.5. CV Builder
3.6. Reporting and Analytics
3.7. Job Application
External Interface Requirements
4.1. User Interfaces
4.2. Software Interfaces
Other Nonfunctional Requirements
1. Introduction <a name="introduction"></a>
1.1. Purpose <a name="purpose"></a>
This document defines the software requirements for the development of a Machine Learning-based CV Recommender and Generator. The software comprises three main modules that utilize different ML models and generative AI, aimed at streamlining the hiring process for companies and job seekers.

1.2. Intended Audience and Reading Suggestions <a name="intended-audience-and-reading-suggestions"></a>
This document is intended for the project development team, stakeholders, and potential users. It is recommended to read this document thoroughly to understand the software’s requirements and functionalities.

1.3. Project Scope <a name="project-scope"></a>
The scope of this project is to create a web-based application that offers an efficient CV recommendation and generation system. It aims to reduce the time and effort involved in the hiring process for companies.

2. Overall Description <a name="overall-description"></a>
2.1. Product Perspective <a name="product-perspective"></a>
The CV Recommender and generation system will consist of three primary modules: Parsing, CV Matcher, and CV Builder. These modules will interact with each other to provide a comprehensive solution.

2.2. Product Features <a name="product-features"></a>
Parsing: Extracting text from CVs and parsing them for relevant information.
Keywords Extraction: Identifying keywords from CVs.
Vector Similarity: Calculating vector similarity for CV-job description matching.
CV Matcher: Weighted matching of CVs with job descriptions and generating a suitability score.
CV Builder: Allowing users to input text to generate professional resumes.
Reporting and Analytics: Providing tools for recruiters to monitor and analyze the hiring process.
Job Application: Enabling users to apply for jobs through the portal with essential fields and auto field completion from a resume.
2.3. User Classes and Characteristics <a name="user-classes-and-characteristics"></a>
The system will cater to two primary user classes:

Companies: These users will utilize the CV Matcher module to match CVs with job descriptions and streamline the hiring process.
Individual Users: These users will use the CV Builder module to create resumes quickly, and they can apply for jobs on the portal.
2.4. Operating Environment <a name="operating-environment"></a>
The system will be a web-based application with the frontend developed using HTML, CSS, and JavaScript. The backend will be implemented using the Django framework.

3. System Features <a name="system-features"></a>
3.1. Parsing <a name="parsing"></a>
3.1.1 Description
The Parsing module is responsible for extracting text from CVs and parsing them to capture relevant information. It will include the ability to identify and separate different sections of a CV, such as contact information, skills, work experience, and education.

3.1.2 Requirements
The system shall accept CV files in various formats (e.g., PDF, Word).
It shall accurately extract and structure text from the CV documents.
Parsing should differentiate between different sections of a CV.
The module should handle a variety of CV layouts and structures.
3.2 Keywords Extraction <a name="keywords-extraction"></a>
3.2.1 Description
The Keywords Extraction module will identify and extract keywords and key phrases from parsed CVs. These keywords will be used for matching CVs with job descriptions.

3.2.2 Requirements
The module shall identify relevant keywords and phrases based on industry-specific criteria.
It shall provide a list of extracted keywords and their associated weight or importance.
3.3 Vector Similarity <a name="vector-similarity"></a>
3.3.1 Description
The Vector Similarity module will calculate the similarity between CVs and job descriptions using vector representations of the text. This will assist in generating suitability scores for CV-job matches.

3.3.2 Requirements
The module shall convert CVs and job descriptions into numerical vector representations.
It shall calculate similarity scores between vectors using appropriate algorithms (e.g., cosine similarity).
The system should generate a suitability score for each CV-job pair.
3.4 CV Matcher <a name="cv-matcher"></a>
3.4.1 Description
The CV Matcher module will provide a weighted matching mechanism to match CVs with job descriptions. It will produce a score indicating how well a candidate's CV matches a specific job description.

3.4.2 Requirements
The module shall consider keyword extraction results for matching.
It shall assign weights to different criteria, such as skills and experience.
The system shall generate a suitability score for each CV and job description pair.
3.5 CV Builder <a name="cv-builder"></a>
3.5.1 Description
The CV Builder module will allow individual users to input text and generate professional CVs based on their provided information. It will assist users in creating well-structured and formatted resumes. This enhanced version will include AI-powered features such as auto field completion from a resume and an AI prompt engineering module to assist candidates in resume building.

3.5.2 Requirements
The module shall provide a user-friendly interface for entering CV information.
It shall offer customizable CV templates and formatting options.
Users should be able to preview and download their generated resumes.
The AI-powered auto field completion feature shall analyze the user's input and suggest relevant content based on their resume and the job description.
The AI prompt engineering module shall provide context-aware prompts and suggestions to help users craft their CV content effectively.
3.6 Reporting and Analytics <a name="reporting-and-analytics"></a>
3.6.1 Description
The Reporting and Analytics module will provide recruiters with tools to monitor and analyze the hiring process. It will include graphical representations and reporting mechanisms to assist recruiters in making informed decisions.

3.6.2 Requirements
The module shall offer graphical representations such as graphs and charts to visualize hiring data.
Recruiters should be able to generate reports on various aspects of the hiring process, including candidate suitability scores, application statistics, and diversity metrics.
The system shall allow recruiters to export reports in common formats (e.g., PDF) for further analysis and sharing.
Recruiters should have the ability to track the progress of job postings and monitor candidate interactions.
3.7 Job Application <a name="job-application"></a>
3.7.1 Description
The Job Application module will enable users to apply for jobs through the portal. It will include essential fields for job applications and incorporate the auto field completion feature from a resume.

3.7.2 Requirements
The module shall provide a standardized job application form with essential fields such as name, contact information, education, and work experience.
Users shall have the option to upload their resumes.
The auto field completion from a resume module shall analyze uploaded resumes and automatically populate relevant fields in the job application form.
Users should have the ability to review and edit auto-populated information before submitting their applications.
4. External Interface Requirements <a name="external-interface-requirements"></a>
4.1 User Interfaces <a name="user-interfaces"></a>
The user interfaces of the ML-based CV Recommender system are designed to provide a user-friendly experience for both companies and individual users. The interfaces will be web-based and follow modern design principles. Here are the key characteristics:

The user interface shall follow HTML, CSS, and JavaScript standards for web-based design.
It will include intuitive navigation menus and controls for easy interaction.
Error message display will follow standard conventions and provide clear error descriptions.
Standard buttons such as "Submit," "Search," and "Download" will appear on relevant screens.
4.2 Software Interfaces <a name="software-interfaces"></a>
The system interfaces with various software components to ensure its functionality. Here are the key software interfaces:

Django Framework: The backend of the system will use the Django web framework for server-side processing.
Web Browsers: The user interfaces are designed to be compatible with modern web browsers such as Chrome, Firefox, and Edge.
Document Processing Libraries: The system may utilize document processing libraries (e.g., Python libraries like PyPDF2 or docx2txt) for parsing CVs.
Machine Learning Libraries: Machine learning models may be implemented using libraries like scikit-learn or TensorFlow.
Database Management System: The system will interact with a database management system for data storage and retrieval.
5. Other Nonfunctional Requirements <a name="other-nonfunctional-requirements"></a>
Data Processing Speed: Parsing, keyword extraction, and vector similarity calculations should be optimized to process CVs swiftly, even for large documents.
Authentication: User identity authentication shall be implemented to ensure that only authorized users can access the system.
Usability: The user interface shall prioritize ease of use to enhance the user experience, with clear navigation and intuitive controls.
Scalability: The system architecture shall support scalability to accommodate a growing user base and increased data processing demands.



