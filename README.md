# LatencyLens

## 📌 Overview

LatencyLens is a Django-based system that deploys across multiple AWS regions and automatically routes traffic to the region with the lowest latency.

## ⚡ Features

- Django app with `/` and `/healthz` endpoints
- Runs in Docker containers on AWS EC2 across multiple regions
- LatencyLens checker script finds the fastest region
- GitHub Actions redeploys to the fastest region automatically
- Django admin logs latency data and switch events

## 🏗 Architecture

1. Multiple EC2 instances run Django in Docker.
2. LatencyLens checker pings `/healthz` endpoints.
3. If a faster region is found → CI/CD redeploys app to that region.
4. Django admin keeps a history of latency & switches.

## 🌍 Target AWS Regions

- us-east-1 (Virginia, USA)
- ap-south-1 (Mumbai, India)

## 📅 Roadmap

- Day 1: Architecture & Repo Setup ✅
- Day 2: Django App Setup
- Day 3: Dockerization
- Day 4: Multi-Region AWS Deployment
- Day 5: LatencyLens Checker Script
- Day 6: CI/CD Integration
- Day 7: Admin Panel Models
- Day 8: Auto-Migration Logic
- Day 9: Dashboard UI
- Day 10: Documentation & Demo
