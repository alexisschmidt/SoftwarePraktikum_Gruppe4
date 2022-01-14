import React, { Component } from 'react';
import AdminTable from '../content/AdminTable';
import AdminSpoText from '../content/AdminSpoText';

class Admin extends Component {
    render(){
        return (
            <div>
                <h1>Hallo Admin</h1>
                <AdminTable />
                <AdminSpoText />
               
            </div>
        )
    }
}

export default Admin;