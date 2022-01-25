import React, { Component } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Input from '@mui/material/Input';

function createData(semester, edvnr, modul, sws, ects, prüfung) {
  return { semester, edvnr, modul, sws, ects, prüfung };
}

const rows = [

    createData(<strong>1</strong>, <strong>VS: 33500</strong>, <strong>Einstufungstest Englisch</strong>, <strong>0</strong>, <strong>0</strong>, <strong>VS: LÜ</strong>),
   
  
    createData(<b>1</b>, <b>PL: 335120</b>, <b>Marketing & Organisation</b>,<b>4</b>,<b>5</b>,<b>PL: KMP</b>),
    createData('','335120a','Marketing',2,2,'Language', 'Literature', 'Sources', 'Connection', 'Description',  'Workload', 'Professor' ),
    createData('','335120b','Organisation',2,3,''),
    createData('', '', '', '', '',''),
  
    createData(<b>1</b>,<b>PL:335121</b>,<b>Grundlagen Wirtschaftsinformatik</b>,<b>4</b> ,<b>5</b>,<b>PL: KMP</b>),
    createData('', '', '', '', '',''),
  
    createData(<b>1</b>,<b>PL:335122</b>,<b>Datenbanken Grundlagen</b>,<b>4</b>,<b>5</b>, <b>PL:KMP</b>),
    createData('','335122a','Vorlesung Datenbanken',2,2,''),
    createData('','335122b','Übung Datenbanken',2,3,''),
    createData('', '', '', '', '',''),
  
    createData(<b>1</b>,<b>PL:335123</b>,<b>Programmieren</b>,<b>4</b>,<b>5</b>,<b>PL:KMP</b>),
    createData('','335123a','Vorlesung Programmieren',2,2,''),
    createData('','335123b','Übung Programmieren',2,3,''),
  

]

export default class AdminTable extends Component {
  constructor(props){
    super(props)
    this.deleteRow = this.deleteRow.bind(this)
  }

  state = {
    editedCell: null,
    rows : rows,

    editedEdvNr: ''
  }

  deleteRow(index){
    // TOOD: send deleted row to backend with index or id
    this.setState({rows: this.state.rows.filter((row, i) => i !== index)})
  }

  saveChangedRow(){
    alert(this.state.editedEdvNr)
    // TODO: send data of changed row to backend
  }

  render(){
    return (
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
          <TableHead>
            <TableRow>
              <TableCell>Semester</TableCell>
              <TableCell align="right">EDV-Nr.</TableCell>
              <TableCell align="right">Modul (Kurzbezeichnung)</TableCell>
              <TableCell align="right">SWS</TableCell>
              <TableCell align="right">ECTS</TableCell>
              <TableCell align="right">Prüfung</TableCell>
              <TableCell align="right">Bearbeiten</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.rows.map((row, index) => (
              <TableRow
                key={row.name}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.semester}
                </TableCell>
                <TableCell align="right">
                  {this.state.editedCell === index ?
                    <Input value={row.edvnr} onChange={e => this.setState({editedEdvNr: e.target.value})} />
                    : 
                    row.edvnr
                  }
                </TableCell>
                <TableCell align="right">
                  {this.state.editedCell === index ?
                    <Input value={row.modul} />
                    : 
                    row.modul
                  }
                </TableCell>
                <TableCell align="right">{row.sws}</TableCell>
                <TableCell align="right">{row.ects}</TableCell>
                <TableCell align="right">{row.prüfung}</TableCell>
                <TableCell align="right">
                  <Button onClick={() => this.setState({editedCell: index})}>Bearbeiten</Button>
                   <Button onClick={() => this.deleteRow(index)}>Löschen</Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }
} 