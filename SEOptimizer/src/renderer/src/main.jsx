import './assets/main.css'

import React from 'react'
import ReactDOM from 'react-dom/client'
import Menu from './pages/Menu'
import Login from './pages/Login'
import { HashRouter, Routes, Route } from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <HashRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/Menu" element={<Menu />} />
      </Routes>
    </HashRouter>
  </React.StrictMode>
)
