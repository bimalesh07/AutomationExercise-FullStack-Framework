pipeline {
    agent any

    // 🎛️ 1. JENKINS DASHBOARD DROPDOWNS SETUP
    parameters {
        choice(
            name: 'RUN_MODE', 
            choices: ['By_Suite_Type', 'By_Specific_File'], 
            description: '1. Pehle select karein ki Suite Type se chalana hai ya kisi ek Single File se.'
        )
        choice(
            name: 'SELECT_SUITE', 
            choices: ['full_regression', 'only_ui', 'only_api', 'smoke'], 
            description: '2. Agar RUN_MODE "By_Suite_Type" hai, toh yahan se selection karein.'
        )
        choice(
            name: 'SELECT_FILE', 
            choices: ['test_login.py', 'test_products.py', 'test_checkout_individual.py', 'test_e2e_order.py'], 
            description: '3. Agar RUN_MODE "By_Specific_File" hai, toh yahan se apni manpasand file chunein.'
        )
    }

    // 🔒 2. ENVIRONMENT VARIABLES (Naam ditto same jo Python code mein use honge)
    environment {
        REPORT_NAME     = "master_automation_report.html"
        
        // 📝 Normal Variables (Automatic Jenkins back-end par create kar dega)
        BASE_URL        = "https://qa-environment.com"
        TEST_USER_EMAIL = "tester_alpha@gmail.com"
        TEST_USER_NAME  = "Alpha Tester"
        
        // 🔒 Secret Password (Jo aapne Jenkins Credentials Manager mein 'MY_SECRET_PASSWORD' ID se save kiya tha)
        DB_PASSWORD     = credentials('MY_SECRET_PASSWORD') 
    }

    stages {
        // 📥 STAGE 1: GitHub se automatic latest code uthana
        stage('Checkout Code') {
            steps {
                echo "Workspace saaf karke GitHub se fresh code pull ho raha hai..."
                cleanWs()
                checkout scm
            }
        }

        // 🛠️ STAGE 2: Python environment, Libraries aur Playwright Setup karna
        stage('Setup Virtual Environment') {
            steps {
                echo "Python Virtual Environment aur Browsers install ho rahe hain..."
                bat '''
                    python -m venv .venv
                    call .venv\\Scripts\\activate
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        // 🏎️ STAGE 3: ASLI EXECUTION (Dono variables aur dropdowns ka combinations)
        stage('Execute Automation Tests') {
            steps {
                script {
                    // CONDITION A: Agar Suite Type chuna hai (UI, API, ya Full Regression)
                    if (params.RUN_MODE == 'By_Suite_Type') {
                        
                        // 1. Pura Blast (UI + API Regression) -> Dono Folders target honge bina kisi tag ke
                        if (params.SELECT_SUITE == 'full_regression') {
                            echo "🚀 RUNNING FULL REGRESSION: Scanning complete UI and API folders..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_ui/ Test_Case/test_api/ -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                        // 2. Sirf UI ka folder run karna
                        else if (params.SELECT_SUITE == 'only_ui') {
                            echo "🌐 RUNNING ONLY UI SUITE (Browser Testing)..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_ui/ -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                        // 3. Sirf API ka folder run karna (Bina Browser, super fast)
                        else if (params.SELECT_SUITE == 'only_api') {
                            echo "🔌 RUNNING ONLY API SUITE (Backend Testing)..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/test_api/ -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                        // 4. Smoke tests jo bikhre hue hain tags ke sahare
                        else {
                            echo "🚬 RUNNING CRITICAL SMOKE TESTS..."
                            bat """
                                call .venv\\Scripts\\activate
                                pytest Test_Case/ -m smoke -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                            """
                        }
                    } 
                    
                    // CONDITION B: Agar dropdown se koi ek specific individual file select ki hai
                    else {
                        echo "🎯 RUNNING SINGLE MODULE FILE: ${params.SELECT_FILE}"
                        bat """
                            call .venv\\Scripts\\activate
                            pytest Test_Case/test_ui/${params.SELECT_FILE} -v -s --html=Reports/${REPORT_NAME} --self-contained-html
                        """
                    }
                }
            }
        }
    }

    // 📊 STAGE 4: Test khatam hone ke baad HTML report automatic Jenkins page par chipkana
    post {
        always {
            echo "Master HTML Report Jenkins dashboard par publish ho rahi hai..."
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