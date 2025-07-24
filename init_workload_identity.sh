#!/bin/bash

GSA="sa-orchestrator@data-engineerig-analitycs-dev.iam.gserviceaccount.com"
PROJECT_ID="data-engineerig-analitycs-dev"
NAMESPACE="airflow"

for KSA in $(kubectl get serviceaccounts -n $NAMESPACE -o jsonpath="{.items[*].metadata.name}"); do
  echo "Vinculando KSA: $KSA"
  gcloud iam service-accounts add-iam-policy-binding "$GSA" \
    --role="roles/iam.workloadIdentityUser" \
    --member="serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA]"
done

for KSA in $(kubectl get serviceaccounts -n $NAMESPACE -o jsonpath="{.items[*].metadata.name}"); do
  echo "Anotando KSA: $KSA"
  kubectl annotate serviceaccount "$KSA" \
    --namespace "$NAMESPACE" \
    iam.gke.io/gcp-service-account="$GSA" \
    --overwrite
done