pipeline {
    agent any
    parameters {
        choice(
            name: 'RUN_MODE', 
            choices: ['By_Suite_Type', 'By_Specific_File'], 
            description: 'Select RUN_MODE: Run whole suite or a specific individual file.'
        )
        choice(
            name: 'SELECT_SUITE', 
            choices: ['full_regression', 'only_ui', 'only_api', 'smoke'], 
            description: 'Suite Selection (Used when RUN_MODE is "By_Suite_Type").'
        )
        choice(
            name: 'SELECT_FILE', 
            choices: [
                'test_product_api.py', 
                'test_register_api.py', 
                'test_cart.py', 
                'test_checkout.py', 
                'test_e2e_order.py', 
                'test_invalid_login.py', 
                'test_login.py', 
                'test_logout.py', 
                'test_products.py', 
                'test_register_existing.py', 
                'test_register.py'
            ], 
            description: 'Individual File Selection (Used when RUN_MODE is "By_Specific_File").'
        )
    }

    // ENVIRONMENT VARIABLES
    environment {
        REPORT_NAME     = "master_automation_report.html"
        BASE_URL        = "https://automationexercise.com"
        TEST_USER_EMAIL = "tester_alpha@gmail.com"
        TEST_USER_NAME  = "Bimalesh Kumar"
        
        // Credentials from Jenkins Credentials Manager
        DB_PASSWORD = credentials('MY_SECRET_PASSWORD') 
    }

    stages {
        //Code Pull from Git
        stage('Checkout Code') {
            steps {
                echo "Cleaning workspace and fetching fresh code from GitHub..."
                cleanWs()
                checkout scm
            }
        }
        // Virtual Env, Libraries aur Runtime .env File Injection
        stage('Setup Virtual Environment') {
            steps {
                echo "Installing Python Dependencies and creating temporary .env file..."
                bat '''
                    :: Virtual Environment logic
                    if not exist .venv (
                        python -m venv .venv
                    )
                    call .venv\\Scripts\\activate
                    pip install -r requirements.txt
                    playwright install

                    :: REATE TEMPORARY .env FILE (Yahan dynamically .env file ban rahi hai)
                    echo BASE_URL=%BASE_URL% > .env
                    echo TEST_USER_EMAIL=%TEST_USER_EMAIL% >> .env
                    echo TEST_USER_NAME=%TEST_USER_NAME% >> .env
                    echo DB_PASSWORD=%DB_PASSWORD% >> .env
                    echo .env file created successfully for this build.
                '''
            }
        }

        //Smart Execution Logic
        stage('Execute Automation Tests') {
            steps {
                script {
                    // CONDITION A: Suite Executions
                    if (params.RUN_MODE == 'By_Suite_Type') {
                        
                        if (params.SELECT_SUITE == 'full_regression') {
                            echo " RUNNING FULL REGRESSION: UI + API Suites..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_ui/ Test_Case/test_api/ -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                        else if (params.SELECT_SUITE == 'only_ui') {
                            echo "RUNNING ONLY UI REGRESSION SUITE..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_ui/ -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                        else if (params.SELECT_SUITE == 'only_api') {
                            echo "RUNNING ONLY API REGRESSION SUITE..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_api/ -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                        else {
                            echo "RUNNING CRITICAL SMOKE TAGS..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/ -m smoke -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                    } 
                    
                    // CONDITION B: Individual File Executions with Dynamic Path Router
                    else {
                        echo "Target File Selected: ${params.SELECT_FILE}"
                        
                        // Smart check to see if the chosen file belongs to API or UI folder
                        if (params.SELECT_FILE.contains('_api.py')) {
                            echo "Routing execution context to API directory..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_api/${params.SELECT_FILE} -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        } else {
                            echo "Routing execution context to UI directory..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_ui/${params.SELECT_FILE} -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                    }
                }
            }
        }
    }

    //HTML Reports Publishing onto Dashboard Dashboard
    post {
        always {
            echo "Publishing Execution Reports onto Jenkins Dashboard View..."
            //DELETE TEMPORARY .env FILE (Test end then  Jenkins  permanently delete env)
            bat 'if exist .env del /f /q .env'
            echo ".env file safely removed from workspace."
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'Reports',
                reportFiles: "${REPORT_NAME}",
                reportName: 'Master Test Execution Report'
            ])
        }
    }
}