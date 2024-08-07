import React, { useState, useEffect } from 'react';
import { useFetchInventory } from './components/api';
import AddInventory from './components/AddInventory';
import RemoveInventory from './components/RemoveInventory';
import InventoryList from './components/InventoryList';
import './App.css';
import { useAuth0 } from '@auth0/auth0-react';

function App() {
    const { loginWithRedirect, logout, isAuthenticated } = useAuth0();
    const fetchInventory = useFetchInventory();
    const [inventory, setInventory] = useState([]);

    const fetchInventoryData = async () => {
        try {
            const data = await fetchInventory();
            setInventory(data);
        } catch (error) {
            console.error('Error fetching inventory:', error);
        }
    };

    useEffect(() => {
        if (isAuthenticated) {
            fetchInventoryData();
        }
    }, [isAuthenticated]);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Inventory Tracking System</h1>
                {isAuthenticated ? (
                    <button onClick={() => logout({ returnTo: window.location.origin })}>Log Out</button>
                ) : (
                    <button onClick={loginWithRedirect}>Log In</button>
                )}
            </header>
            {isAuthenticated && (
                <main>
                    <section>
                        <h2>Add to Inventory</h2>
                        <AddInventory fetchInventoryData={fetchInventoryData} />
                    </section>
                    <section>
                        <h2>Remove from Inventory</h2>
                        <RemoveInventory fetchInventoryData={fetchInventoryData} />
                    </section>
                    <section>
                        <h2>Inventory List</h2>
                        <InventoryList inventory={inventory} />
                    </section>
                </main>
            )}
        </div>
    );
}

export default App;
