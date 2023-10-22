curl --request POST \
     --url https://api.tryterra.co/v2/auth/generateWidgetSession \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'dev-id: golapicare-staging-RVAcl5Mtck' \
     --header 'x-api-key: fMcpCMF579LF8fYlFDwLq-EO4o_xpsQ0' \
     --data '
{
  "providers": "GARMIN,WITHINGS,FITBIT,GOOGLE,OURA,WAHOO,PELOTON,ZWIFT,TRAININGPEAKS,FREESTYLELIBRE,DEXCOM,COROS,HUAWEI,OMRON,RENPHO,POLAR,SUUNTO,EIGHT,APPLE,CONCEPT2,WHOOP,IFIT,TEMPO,CRONOMETER,FATSECRET,NUTRACHECK,UNDERARMOUR",
  "language": "en"
}