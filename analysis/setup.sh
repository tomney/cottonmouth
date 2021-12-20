SERVICE_ACCOUNT_NAME=$1

# Create service account
gcloud iam service-accounts create cottonmouth --display-name="cottonmouth" --role='roles/bigquery.dataEditor'
gcloud iam service-accounts add-iam-policy-binding cottonmouth --role='roles/bigquery.dataEditor'