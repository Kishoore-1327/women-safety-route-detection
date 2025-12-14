# Women Safety Route Detection 🚨🗺️

An AI-powered full-stack web application that predicts the safest travel routes for women using historical crime data, risk analysis, and interactive maps.

---

## 📌 Problem Statement
Women often face safety concerns while traveling, especially in unfamiliar areas. Existing navigation systems focus only on distance and time, not safety. This project addresses that gap by analyzing crime data to recommend safer routes.

---

## 🎯 Objectives
- Predict route safety using historical crime data  
- Classify routes as **Safe**, **Moderate Risk**, or **High Risk**  
- Visualize routes and crime hotspots on an interactive map  
- Provide emergency SOS alert functionality  

---

## 🛠️ Tech Stack

### Frontend
- React.js
- Leaflet.js (Maps)
- OpenStreetMap
- OpenRouteService API

### Backend
- Python
- Flask
- Machine Learning (Scikit-learn)
- REST APIs

### Data
- Historical crime dataset (CSV)
- Geospatial coordinates (latitude, longitude)

---

## 🚀 Features
- 📍 Source & destination based route analysis  
- 🟢🟠🔴 Route risk classification  
- ⚠️ Crime hotspot visualization  
- 🗺️ Real map-based route rendering  
- 📱 SOS alert system for emergencies  

---

## 🧠 How It Works
1. User enters source and destination  
2. Addresses are geocoded into coordinates  
3. Route is fetched using OpenRouteService  
4. Crime data near the route is analyzed  
5. Risk score and safety category are calculated  
6. Results are visualized on an interactive map  

---

## 📂 Project Structure

