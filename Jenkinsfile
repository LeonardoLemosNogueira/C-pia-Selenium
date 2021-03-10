pipeline {
  agent any // Replace by specific label for narrowing down to OutSystems pipeline-specific agents. A dedicated agent will be allocated for the entire pipeline run.
  
  options { skipStagesAfterUnstable() }

  stages {
    stage('Install Python Dependencies') {
      steps {
        // Only the virtual environment needs to be installed at the system level
        // Install the rest of the dependencies at the environment level and not the system level
        withPythonEnv('python') {
          echo "Install Python requirements"
          bat 'pip install -r requirements.txt --no-index'
        }
      }
    }
    stage('Run Selenium') {
      steps {
        withPythonEnv('python') {
          // Generate the URL endpoints of the BDD tests
          powershell "python -m src\gerador_resultado"
        }
      }
    }
  }
}
//     stage('BDD Tests') {
//       steps {
//         echo "BDD Tests"
//         }
//       }
//     stage('Selenium Tests') {
//       steps {
//         echo "Selenium Tests"
//         }
//       }
//     stage('Deploy Application') {
//       steps {
//         echo "Deploy Application"
//         }
//       }   
//   }
// }