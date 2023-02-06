pipeline {
  agent any
  stages {
    stage('backup') {
      steps {
        sh 'python3.8 bckrst.py backup'
      }
    }
    stage('restore') {
      steps {
        sh 'python3.8 bckrst.py restore'
      }
    }
  }
}
