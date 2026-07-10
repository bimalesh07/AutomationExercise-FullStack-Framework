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
    environment {
        REPORT_NAME     = "master_automation_report.html"
        base_url        = "https://automationexercise.com"
        API_BASE_URL    = "https://automationexercise.com/api/"
        email           = "bimlaesh@gmail.com"
        password        = "123456bky" 
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Cleaning workspace and fetching fresh code from GitHub..."
                cleanWs()
                checkout scm
            }
        }
        
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

                    (echo base_url=%base_url%)>.env
                    (echo API_BASE_URL=%API_BASE_URL%)>>.env
                    (echo email=%email%)>>.env
                    (echo password=%password%)>>.env
                    echo .env file created successfully for this build.
                '''
            }
        }

        stage('Execute Automation Tests') {
            steps {
                script {
                    if (params.RUN_MODE == 'By_Suite_Type') {
                        if (params.SELECT_SUITE == 'full_regression') {
                            echo " RUNNING FULL REGRESSION: UI + API Suites..."
                            bat "call .venv\\Scripts\\activate && pytest Test_Case/test_ui/ Test_Case/test_api/ -v -s --html=Reports/${env.REPORT_NAME} --self-contained-html"
                        }
                        else if (params.SELECT_SUITE == 'only_ui') {
                            echo "RUNNING ONLY UI REGRESSION SUITE..."
                            bat "call .venv\\Scripts\\activate && pytest Test_Case/test_ui/ -v -s --html=Reports/${env.REPORT_NAME} --self-contained-html"
                        }
                        else if (params.SELECT_SUITE == 'only_api') {
                            echo "RUNNING ONLY API REGRESSION SUITE..."
                            bat "call .venv\\Scripts\\activate && pytest Test_Case/test_api/ -v -s --html=Reports/${env.REPORT_NAME} --self-contained-html"
                        }
                        else {
                            echo "RUNNING CRITICAL SMOKE TAGS..."
                            bat "call .venv\\Scripts\\activate && pytest Test_Case/ -m smoke -v -s --html=Reports/${env.REPORT_NAME} --self-contained-html"
                        }
                    } 
                    else {
                        echo "Target File Selected: ${params.SELECT_FILE}"
                        if (params.SELECT_FILE.contains('_api.py')) {
                            echo "Routing execution context to API directory..."
                            bat "call .venv\\Scripts\\activate && pytest Test_Case/test_api/${params.SELECT_FILE} -v -s --html=Reports/${env.REPORT_NAME} --self-contained-html"
                        } else {
                            echo "Routing execution context to UI directory..."
                            bat "call .venv\\Scripts\\activate && pytest Test_Case/test_ui/${params.SELECT_FILE} -v -s --html=Reports/${env.REPORT_NAME} --self-contained-html"
                        }
                    }
                }
            }
        }
        stage('Execute Performance Tests') {
            steps {
                script {
                    echo "Running Automated UI Load Test via JMeter..."
                    bat "if exist Reports\\jmeter_results.csv del /f /q Reports\\jmeter_results.csv"
                    
                   bat """
                         call "C:\\apache-jmeter-5.6.3\\bin\\jmeter" -n -t Performance_Tests/load_test.jmx -l Reports/jmeter_results.csv
                     """
                    echo "JMeter Performance Testing Completed!"
                }
            }
        }
    } 

    post {
        always {
            script {
                echo "Publishing Execution Reports onto Jenkins Dashboard View..."
                bat 'if exist .env del /f /q .env'
                echo ".env file safely removed from workspace."
                
                publishHTML(target: [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'Reports',
                    reportFiles: "${env.REPORT_NAME}",
                    reportName: 'Full Test Execution Report'
                ])
            }
        }
    }
}