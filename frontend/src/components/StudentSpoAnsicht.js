import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { withStyles } from '@material-ui/core';

import Box from '@mui/material/Box';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import API from '../api/API';



class StudentSpoAnsicht extends Component {

    constructor(props) {
        super(props);

        this.state = {
            user: null,
            spo: null,
            studycourses: [],
			modules: [],
			moduleparts: [],
			semester: [],
            loadingProgress: false,
            error: null,

            
            spoFormIsOpen: false,
            moduleFormOpen: false,
            modulepartFormOpen: false,
            selectedSPO:null,
            selectedModule:null, 
            selectedModulePart:null,
            // müssen die zwei auch sein oder nur selectedspo?
            
            spoId: null,
            studyCourseId: null


        };
    }

 

    getAllStudycoursesById = () => {
        const id = this.props.match.params.id;
        API.getAPI().getAllStudycoursesById(id).then(studyCoursebo => {            
            this.setState({
                studycourses: studyCoursebo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                studycourses: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getUser = (hash) => {
        API.getAPI().getUser(hash).then(userbo => {            
            this.setState({
                user: userbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                user: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getPerson = (hash) => {
        API.getAPI().getPerson(hash).then(personbo => {            
            this.setState({
                person: personbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                person: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

	getAllModulesBySpoHash= (hash) => {

        const api = API.getAPI();
        
        api.getSpo(hash).then(spo => {

            this.setState({
                spo: {...spo, modules: []},
                loadingProgress: false,
                error: null
            });

            
            spo.modules.forEach(moudleHash => {
                api.getModuleByHash(moudleHash).then(m => {                

                    api.getModulePartByHash(moudleHash).then(modulePart => {
                        
                        if (m && m.length) {
                            let newModule = m[0];
                            newModule.moduleparts = modulePart;

                            this.setState({
                                spo: { ...this.state.spo, modules: [...this.state.spo.modules, newModule] }
                            });
                        } else {
                            this.setState({
                                spo: { ...this.state.spo, modules: [...m] }
                            });
                        }
                    });                    
                });
            });
        });

        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getSemsterFromModule(element) {
        if (element) {
            if (element.moduleparts && element.moduleparts.length >= 1) {
                return `${element.moduleparts[0].semester}`;
            }
        } 
        return '1'
    }
    

    componentDidMount() {
        const { classes, user } = this.props;

        this.setState({
            user: user,
        });

        this.getAllModulesBySpoHash(user.spo);
    }

    render() {
        const { classes, bearbeitenBoolean } = this.props;
        const { loadingProgress, error, studycourses, modules, moduleparts, semester, person, spo, user, spoFormIsOpen, moduleFormOpen, modulepartFormOpen, selectedSPO, selectedModule, selectedModulepart} = this.state;
        return (
            <>
                        <Box sx={{ width: '100%', maxWidth: 650, marginLeft: 'auto', marginRight: 'auto' }} className="admin-spo-container">
            <div>
                <Card>
                    <CardContent>

                        <div className="admin-spo-box fix-header-box">
                            
                            <div className="admin-spo-box-semster">
                                Semester
                            </div>

                            <div className="admin-spo-box-edv">
                                EDV-Nr.
                            </div>

                            <div className="admin-spo-box-module">
                                Modul (Kursbezeichnung)
                            </div>

                            <div className="admin-spo-box-sws">
                                SWS
                            </div>

                            <div className="admin-spo-box-ects">
                                ECTS
                            </div>

                            <div className="admin-spo-box-pruefung">
                                Prüfung
                            </div> 
                        </div>

                        {
                            spo?.modules?.map((moduleElement) => {
                                return (
                                    <>
                                    <Accordion key={moduleElement.id}>
                                    <AccordionSummary
                                        expandIcon={<ExpandMoreIcon />}
                                        aria-controls="panel1a-content"
                                        id="panel1a-header"
                                        >
                                    <div className="admin-spo-box fix-header-box">

                                        <div className="admin-spo-box-semster">
                                            {/* TODO ALexis. Wenn backend ready, erstze alle static daten mit den aus der dantenbank. module sollte das modul object sein"! */}
                                            {/* {moduleElement.id} */}
                                            {this.getSemsterFromModule(moduleElement)}
                                        </div>

                                        <div className="admin-spo-box-edv">
                                            {moduleElement.edvnr}
                                        </div>

                                        <div className="admin-spo-box-module">
                                            {moduleElement.name}
                                        </div>

                                        <div className="admin-spo-box-sws">
                                            
                                        </div>

                                        <div className="admin-spo-box-ects">
                                            {moduleElement.ects}
                                        </div>

                                        <div className="admin-spo-box-pruefung">
                                        	{moduleElement.examtype}              
                                        </div>                                        

                                    </div>
                                    </AccordionSummary>
                                                    <AccordionDetails>
                                                       

                                                        <table cellPadding="8">
                                                            <tbody>
                                                            <tr>
                                                            <td>Title</td>
                                                            <td>{moduleElement.title}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Language</td>
                                                            <td>{moduleElement.outcome}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Literature</td>
                                                            <td>{moduleElement.requirement}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Sources</td>
                                                            <td>{moduleElement.type}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Connection</td>
                                                            <td>{moduleElement.workload}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Instructor</td>
                                                            <td>{moduleElement.instructor}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Createdby</td>
                                                            <td>{moduleElement.createdby}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Creationdate</td>
                                                            <td>{moduleElement.creationdate}</td>
                                                            </tr>
                                                            </tbody>
                                                        </table>
                                                        
                                                    </AccordionDetails>
                                                </Accordion>
                                    
                                    {
                                        moduleElement?.moduleparts?.map((modulePartElement) => {
                                
                                            return (
                                                <Accordion key={modulePartElement.id}>
                                                    <AccordionSummary
                                                        expandIcon={<ExpandMoreIcon />}
                                                        aria-controls="panel1a-content"
                                                        id="panel1a-header"
                                                    >
                                                        <div className="admin-spo-accord-box">

                                                            <div className="admin-spo-accord-box-semster">
                                                                {modulePartElement.semester}
                                                            </div>

                                                            <div className="admin-spo-box-edv">
                                                                {/* TODO ALexis. Wenn backend ready, erstze alle static daten mit den aus der dantenbank. modulePartElement sollte das part modul object sein"! */}
                                                                {modulePartElement.edvnr}
                                                            </div>

                                                            <div className="admin-spo-accord-box-module">
                                                                {modulePartElement.name}
                                                            </div>

                                                            <div className="admin-spo-accord-box-sws">
                                                                {modulePartElement.sws}
                                                            </div>

                                                            <div className="admin-spo-accord-box-ects">
                                                                {modulePartElement.ects}
                                                            </div>
                                                        </div>
                                                    </AccordionSummary>
                                                    <AccordionDetails>
                                                        <table cellPadding="8">
                                                            <tbody>
                                                            <tr>
                                                            <td>Language</td>
                                                            <td>{modulePartElement.language}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Literature</td>
                                                            <td>{modulePartElement.literature}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Sources</td>
                                                            <td>{modulePartElement.sources}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Connection</td>
                                                            <td>{modulePartElement.connection}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Description</td>
                                                            <td>{modulePartElement.description}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Workload</td>
                                                            <td>{modulePartElement.workload}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Professor</td>
                                                            <td>{modulePartElement.professor}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Creationdate</td>
                                                            <td>{modulePartElement.creationdate}</td>
                                                            </tr>
                                                            </tbody>
                                                        </table>
                                                    </AccordionDetails>
                                                </Accordion>
                                            )
                                        })
                                    }
                                    </>
                                )
                            })
                        }

                            
                    </CardContent>
                </Card>
            </div>
        </Box>
              </>
        )
    }


}
/** Component specific styles */
const styles = theme => ({
    root: {
        width: '100%',
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
    },
    content: {
        margin: theme.spacing(1),
    },
    table: {
        minWidth: 700,
    },
    header:{
        marginBottom: theme.spacing(1),
        paddingLeft: theme.spacing(1),
        paddingRight: theme.spacing(1),
    },
    button:{
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(3),
        float: 'right'
    }
});

/** PropTypes */
StudentSpoAnsicht.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** @ignore */
    location: PropTypes.object.isRequired,
   
}


export default withRouter(withStyles(styles)(StudentSpoAnsicht));