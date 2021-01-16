'''
  this is a list of useful commands in terminal (cmd) to create React app
  for more info: https://reactjs.org/
'''

### Prerequisites
- Make sure you have a recent version of [Node.js](https://nodejs.org/en/) installed

### Create New React App
- "cd" to the relevant folder
- run next command: "npx create-react-app <NAME-OF-APP>"

### Runs the app in development mode
- run next command: "cd <NAME-OF-APP>"
- run next command: "npm start"
- open browser in the next url: http://localhost:3000

### build production to deploy in AWS S3
- run next command: "cd <NAME-OF-APP>"
- run next command: "npm run build"
- a new folder "build" will be created in the app folder, upload all the folder contains to AWS S3 bucket
- Use this bucket to host a website by going to "Properties" -> "Static website hosting"
- give this bucket the next policy:
                                    {
                                        "Version": "2012-10-17",
                                        "Statement": [
                                            {
                                                "Sid": "WebsiteAllowGET",
                                                "Effect": "Allow",
                                                "Principal": "*",
                                                "Action": "s3:GetObject",
                                                "Resource": "arn:aws:s3:::<BUCKET-NAME>/*"
                                            }
                                        ]
                                    }
