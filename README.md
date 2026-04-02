# Project: WoW Addon Auto-Sell Validation Plan
> **Objective:** Ensure 100% accuracy in automated vendor-sale logic to prevent accidental deletion of high-value player assets.

## 📋 Test Strategy
This project focuses on the functional validation of a "Grey/White Item Auto-Seller" logic. The goal is to verify that the system correctly identifies item rarity and protects "Soulbound" or "User-Whitelisted" items.

## 🛠️ Tools & Environment
*   **Language:** Python 3.14
*   **Frameworks:** Selenium (Web-based Armory validation), PyTest (Logic testing)
*   **Platform:** Windows 11 / Firefox / Selenium

## 🧪 High-Level Test Cases
| ID | Test Scenario | Expected Result | Priority |
|:---|:--- |:--- |:---|
| TC-01 | Sell "Poor" (Grey) Quality Item | Item is moved to vendor tray and sold. | High |
| TC-02 | Attempt to Sell "Epic" (Purple) Quality | System ignores item; item remains in bags. | Critical |
| TC-03 | User Whitelist Override | "Poor" item on whitelist is protected from sale. | Medium |
| TC-04 | Inventory Full Condition | System triggers "Inventory Full" warning and stops. | High |

## 🚀 Automation Roadmap
1. [x] Manual Validation Plan Created
2. [ ] Local Python environment configured
3. [ ] Basic Logic script (Unit Tests for item ID filtering)
4. [ ] Selenium integration for Web-based asset verification
