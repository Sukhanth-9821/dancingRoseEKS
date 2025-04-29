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
                    withCredentials([usernamePassword(credentialsId: 'aws-creds',usernameVariable:"AWS_ACCESS_KEY_ID",passwordVariable:"AWS_SECRET_ACCESS_KEY" )])
                        {
                    sh "aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID"
                    sh "aws configure set aws_secret_access_key  $AWS_SECRET_ACCESS_KEY"
                    sh "aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 838676815759.dkr.ecr.ap-south-1.amazonaws.com"
                    sh 'sudo docker build -t dancingrose/kubernetes .'
                    sh 'sudo docker tag dancingrose/kubernetes:latest 838676815759.dkr.ecr.ap-south-1.amazonaws.com/dancingrose/kubernetes:${IMAGE_TAG}'
                    sh "sudo docker push 838676815759.dkr.ecr.ap-south-1.amazonaws.com/dancingrose/kubernetes:latest"
                        }
                }
            }
        }

    }
}