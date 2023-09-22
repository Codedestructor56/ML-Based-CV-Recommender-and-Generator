<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>ML-Based CV Recommender and Generator</h1>

<p><strong>Version 1.0</strong></p>

<h2>Project Team:</h2>
<ul>
    <li>Supervisor: Obad Zafar</li>
    <li>Team Leader: Syed Shahzain Hassan</li>
    <li>Team Members: Abdul Moiz Abid, Sufyan Siddiqui, Muhammad Sameed Fayiz, Muhammad Ammar</li>
</ul>

<p><strong>Date: September 09, 2023</strong></p>

<h2>Table of Contents</h2>
<ol>
    <li><a href="#introduction">Introduction</a></li>
    <ul>
        <li><a href="#purpose">1.1 Purpose</a></li>
        <li><a href="#intended-audience-and-reading-suggestions">1.2 Intended Audience and Reading Suggestions</a></li>
        <li><a href="#project-scope">1.3 Project Scope</a></li>
    </ul>
    <li><a href="#overall-description">Overall Description</a></li>
    <ul>
        <li><a href="#product-perspective">2.1 Product Perspective</a></li>
        <li><a href="#product-features">2.2 Product Features</a></li>
        <li><a href="#user-classes-and-characteristics">2.3 User Classes and Characteristics</a></li>
        <li><a href="#operating-environment">2.4 Operating Environment</a></li>
    </ul>
    <li><a href="#system-features">System Features</a></li>
    <ul>
        <li><a href="#parsing">3.1 Parsing</a></li>
        <li><a href="#keywords-extraction">3.2 Keywords Extraction</a></li>
        <li><a href="#vector-similarity">3.3 Vector Similarity</a></li>
        <li><a href="#cv-matcher">3.4 CV Matcher</a></li>
        <li><a href="#cv-builder">3.5 CV Builder</a></li>
        <li><a href="#reporting-and-analytics">3.6 Reporting and Analytics</a></li>
        <li><a href="#job-application">3.7 Job Application</a></li>
    </ul>
    <li><a href="#external-interface-requirements">External Interface Requirements</a></li>
    <ul>
        <li><a href="#user-interfaces">4.1 User Interfaces</a></li>
        <li><a href="#software-interfaces">4.2 Software Interfaces</a></li>
    </ul>
    <li><a href="#other-nonfunctional-requirements">Other Nonfunctional Requirements</a></li>
</ol>

<h2 id="introduction">1. Introduction</h2>

<h3 id="purpose">1.1 Purpose</h3>
<p>The purpose of this document is to define the software requirements for the development of a Machine Learning-based CV Recommender and Generator. The software comprises three main modules that utilize different ML models and generative AI, aimed at streamlining the hiring process for companies and job seekers.</p>

<h3 id="intended-audience-and-reading-suggestions">1.2 Intended Audience and Reading Suggestions</h3>
<p>This document is intended for the project development team, stakeholders, and potential users. It is recommended to read this document thoroughly to understand the software’s requirements and functionalities.</p>

<h3 id="project-scope">1.3 Project Scope</h3>
<p>The scope of this project is to create a web-based application that offers an efficient CV recommendation and generation system. It aims to reduce the time and effort involved in the hiring process for companies.</p>

<h2 id="overall-description">2. Overall Description</h2>

<h3 id="product-perspective">2.1 Product Perspective</h3>
<p>The CV Recommender and generation system will consist of three primary modules: Parsing, CV Matcher, and CV Builder. These modules will interact with each other to provide a comprehensive solution.</p>

<h3 id="product-features">2.2 Product Features</h3>
<ul>
    <li><strong>Parsing:</strong> Extracting text from CVs and parsing them for relevant information.</li>
    <li><strong>Keywords Extraction:</strong> Identifying keywords from CVs.</li>
    <li><strong>Vector Similarity:</strong> Calculating vector similarity for CV-job description matching.</li>
    <li><strong>CV Matcher:</strong> Weighted matching of CVs with job descriptions and generating a suitability score.</li>
    <li><strong>CV Builder:</strong> Allowing users to input text to generate professional resumes.</li>
    <li><strong>Reporting and Analytics:</strong> Providing tools for recruiters to monitor and analyze the hiring process.</li>
    <li><strong>Job Application:</strong> Enabling users to apply for jobs through the portal with essential fields and auto field completion from a resume.</li>
</ul>

<h3 id="user-classes-and-characteristics">2.3 User Classes and Characteristics</h3>
<p>The system will cater to two primary user classes:</p>
<ul>
    <li><strong>Companies:</strong> These users will utilize the CV Matcher module to match CVs with job descriptions and streamline the hiring process.</li>
    <li><strong>Individual Users:</strong> These users will use the CV Builder module to create resumes quickly, and they can apply for jobs on the portal.</li>
</ul>

<h3 id="operating-environment">2.4 Operating Environment</h3>
<p>The system will be a web-based application with the frontend developed using HTML, CSS, and JavaScript. The backend will be implemented using the Django framework.</p>

<h2 id="system-features">3. System Features</h2>

<h3 id="parsing">3.1 Parsing</h3>

<h4 id="3.1.1 Description">3.1.1 Description</h4>
<p>The Parsing module is responsible for extracting text from CVs and parsing them to capture relevant information. It will include the ability to identify and separate different sections of a CV, such as contact information, skills, work experience, and education.</p>

<h4 id="3.1.2 Requirements">3.1.2 Requirements</h4>
<ul>
    <li>The system shall accept CV files in various formats (e.g., PDF, Word).</li>
    <li>It shall accurately extract and structure text from the CV documents.</li>
    <li>Parsing should differentiate between different sections of a CV.</li>
    <li>The module should handle a variety of CV layouts and structures.</li>
</ul>

<h3 id="keywords-extraction">3.2 Keywords Extraction</h3>

<h4 id="3.2.1 Description">3.2.1 Description</h4>
<p>The Keywords Extraction module will identify and extract keywords and key phrases from parsed CVs. These keywords will be used for matching CVs with job descriptions.</p>

<h4 id="3.2.2 Requirements">3.2.2 Requirements</h4>
<ul>
    <li>The module shall identify relevant keywords and phrases based on industry-specific criteria.</li>
    <li>It shall provide a list of extracted keywords and their associated weight or importance.</li>
</ul>

<h3 id="vector-similarity">3.3 Vector Similarity</h3>

<h4 id="3.3.1 Description">3.3.1 Description</h4>
<p>The Vector Similarity module will calculate the similarity between CVs and job descriptions using vector representations of the text. This will assist in generating suitability scores for CV-job matches.</p>

<h4 id="3.3.2 Requirements">3.3.2 Requirements</h4>
<ul>
    <li>The module shall convert CVs and job descriptions into numerical vector representations.</li>
    <li>It shall calculate similarity scores between vectors using appropriate algorithms (e.g., cosine similarity).</li>
    <li>The system should generate a suitability score for each CV-job pair.</li>
</ul>

<h3 id="cv-matcher">3.4 CV Matcher</h3>

<h4 id="3.4.1 Description">3.4.1 Description</h4>
<p>The CV Matcher module will provide a weighted matching mechanism to match CVs with job descriptions. It will produce a score indicating how well a candidate's CV matches a specific job description.</p>

<h4 id="3.4.2 Requirements">3.4.2 Requirements</h4>
<ul>
    <li>The module shall consider keyword extraction results for matching.</li>
    <li>It shall assign weights to different criteria, such as skills and experience.</li>
    <li>The system shall generate a suitability score for each CV and job description pair.</li>
</ul>

<h3 id="cv-builder">3.5 CV Builder</h3>

<h4 id="3.5.1 Description">3.5.1 Description</h4>
<p>The CV Builder module will allow individual users to input text and generate professional CVs based on their provided information. It will assist users in creating well-structured and formatted resumes. This enhanced version will include AI-powered features such as auto field completion from a resume and an AI prompt engineering module to assist candidates in resume building.</p>

<h4 id="3.5.2 Requirements">3.5.2 Requirements</h4>
<ul>
    <li>The module shall provide a user-friendly interface for entering CV information.</li>
    <li>It shall offer customizable CV templates and formatting options.</li>
    <li>Users should be able to preview and download their generated resumes.</li>
    <li>The AI-powered auto field completion feature shall analyze the user's input and suggest relevant content based on their resume and the job description.</li>
    <li>The AI prompt engineering module shall provide context-aware prompts and suggestions to help users craft their CV content effectively.</li>
</ul>

<h3 id="reporting-and-analytics">3.6 Reporting and Analytics</h3>

<h4 id="3.6.1 Description">3.6.1 Description</h4>
<p>The Reporting and Analytics module will provide recruiters with tools to monitor and analyze the hiring process. It will include graphical representations and reporting mechanisms to assist recruiters in making informed decisions.</p>

<h4 id="3.6.2 Requirements">3.6.2 Requirements</h4>
<ul>
    <li>The module shall offer graphical representations such as graphs and charts to visualize hiring data.</li>
    <li>Recruiters should be able to generate reports on various aspects of the hiring process, including candidate suitability scores, application statistics, and diversity metrics.</li>
    <li>The system shall allow recruiters to export reports in common formats (e.g., PDF) for further analysis and sharing.</li>
    <li>Recruiters should have the ability to track the progress of job postings and monitor candidate interactions.</li>
</ul>

<h3 id="job-application">3.7 Job Application</h3>

<h4 id="3.7.1 Description">3.7.1 Description</h4>
<p>The Job Application module will enable users to apply for jobs through the portal. It will include essential fields for job applications and incorporate the auto field completion feature from a resume.</p>

<h4 id="3.7.2 Requirements">3.7.2 Requirements</h4>
<ul>
    <li>The module shall provide a standardized job application form with essential fields such as name, contact information, education, and work experience.</li>
    <li>Users shall have the option to upload their resumes.</li>
    <li>The auto field completion from a resume module shall analyze uploaded resumes and automatically populate relevant fields in the job application form.</li>
    <li>Users should have the ability to review and edit auto-populated information before submitting their applications.</li>
</ul>

<h2 id="external-interface-requirements">4. External Interface Requirements</h2>

<h3 id="user-interfaces">4.1 User Interfaces</h3>
<p>The user interfaces of the ML-based CV Recommender system are designed to provide a user-friendly experience for both companies and individual users. The interfaces will be web-based and follow modern design principles. Here are the key characteristics:</p>
<ul>
    <li>The user interface shall follow HTML, CSS, and JavaScript standards for web-based design.</li>
    <li>It will include intuitive navigation menus and controls for easy interaction.</li>
    <li>Error message display will follow standard conventions and provide clear error descriptions.</li>
    <li>Standard buttons such as "Submit," "Search," and "Download" will appear on relevant screens.</li>
</ul>

<h3 id="software-interfaces">4.2 Software Interfaces</h3>
<p>The system interfaces with various software components to ensure its functionality. Here are the key software interfaces:</p>
<ul>
    <li>Django Framework: The backend of the system will use the Django web framework for server-side processing.</li>
    <li>Web Browsers: The user interfaces are designed to be compatible with modern web browsers such as Chrome, Firefox, and Edge.</li>
    <li>Document Processing Libraries: The system may utilize document processing libraries (e.g., Python libraries like PyPDF2 or docx2txt) for parsing CVs.</li>
    <li>Machine Learning Libraries: Machine learning models may be implemented using libraries like scikit-learn or TensorFlow.</li>
    <li>Database Management System: The system will interact with a database management system for data storage and retrieval.</li>
</ul>

<h2 id="other-nonfunctional-requirements">5. Other Nonfunctional Requirements</h2>
<ul>
    <li><strong>Data Processing Speed:</strong> Parsing, keyword extraction, and vector similarity calculations should be optimized to process CVs swiftly, even for large documents.</li>
    <li><strong>Authentication:</strong> User identity authentication shall be implemented to ensure that only authorized users can access the system.</li>
    <li><strong>Usability:</strong> The user interface shall prioritize ease of use to enhance the user experience, with clear navigation and intuitive controls.</li>
    <li><strong>Scalability:</strong> The system architecture shall support scalability to accommodate a growing user base and increased data processing demands.</li>
</ul>

</body>
</html>




