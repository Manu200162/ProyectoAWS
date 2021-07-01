#!/bin/bash
DEPLOYMENT_BUCKET="fedex-bucket-8888"
STACK_NAME="fedEx-app"

while getopts ":bdpw" OPTION; do
    case $OPTION in
    d)
      DEPLOY=1
      ;;
    w)
      WEBSITE=1
      ;;
    p)
      PACKAGE=1
      ;;
    b)
      BUILD=1
      ;;
    *)
      ;;
    esac
done

if [[ $BUILD == 1 ]]
then
    pip3 install --target package -r requirements.txt
    cp -a src/. package/
fi

if [[ $PACKAGE == 1 ]]
then
    aws cloudformation package --template-file template.yaml --s3-bucket $DEPLOYMENT_BUCKET --output-template-file packaged-template.json
fi

if [[ $DEPLOY == 1 ]]
then
    aws cloudformation deploy --template-file packaged-template.json --stack-name $STACK_NAME --capabilities CAPABILITY_NAMED_IAM
fi

if [[ $WEBSITE == 1 ]]
then
    aws s3 cp website s3://fedex-bucket-website-123/ --recursive
    
fi