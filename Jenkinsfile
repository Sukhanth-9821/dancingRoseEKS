pipeline{
    agent any
    environment{
        AWS_ACCOUNT_ID="838676815759"
        AWS_DEFAULT_REGION="ap-south-1"
        IMAGE_REPO_NAME="qwer"
        IMAGE_TAG="Latest"
        REPOSITORY_URI="qewrr"

    }

    stages{
        stage ("buid stage"){
            steps{
                script{
                    echo "This is simple build stage"
                }
            }
        }

        stage("docker image build"){
            steps{
                script{
                    sh 'export AWS_ACCESS_KEY_ID=AKIA4GRIIT6HYRUNHHN2'
                    sh 'export AWS_SECRET_ACCESS_KEY=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'
                    sh "aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 838676815759.dkr.ecr.ap-south-1.amazonaws.com"
                    sh 'docker build -t dancingrose/kubernetes .'
                    sh 'docker tag dancingrose/kubernetes:latest 838676815759.dkr.ecr.ap-south-1.amazonaws.com/dancingrose/kubernetes:${IMAGE_TAG}'
                    sh "docker push 838676815759.dkr.ecr.ap-south-1.amazonaws.com/dancingrose/kubernetes:latest"
                }
            }
        }

    }
}