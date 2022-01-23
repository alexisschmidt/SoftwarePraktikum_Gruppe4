import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { withStyles } from '@material-ui/core';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import API from '../api/API';
import ContextErrorMessage from './dialogs/ContextErrorMessage';
import LoadingProgress from './dialogs/LoadingProgress';
import AllStudycoursesEntry from './AllStudycoursesEntry';
import { useNavigate } from "react-router-dom";


class AdminSpoAnsicht extends Component {

    constructor(props) {
        super(props);

        this.state = {
            studycourses: [],
			modules: [],
			moduleparts: [],
			semester: [],
            loadingProgress: false,
            error: null,
            //showStudiengangAnlegenForm: false

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

	getAllModulesById = () => {
        API.getAPI().getAllModulesById().then(modulebo => {            
            this.setState({
                modules: modulebo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                modules: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

	getAllModulePartsById = () => {
        API.getAPI().getAllModulePartsById().then(modulepartbo => {            
            this.setState({
                moduleparts: modulepartbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                moduleparts: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

	getAllSemesterById = () => {
        API.getAPI().getAllSemesterById().then(semesterbo => {            
            this.setState({
                semester: semesterbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                semester: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }


    getAllPersonsById = () => {
        API.getAPI().getAllPersonsById().then(personbo => {            
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

    getAllSposById = () => {
        API.getAPI().getAllSposById().then(spobo => {            
            this.setState({
                spo: spobo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                semester: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getAllUsersById = () => {
        API.getAPI().getAllUsersById().then(userbo => {            
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

    CreateStudycoursesFormClosed = event => {
        this.setState({
            showCreateStudycoursesForm: false,
        })
    }

    buttonNavigateToCourseClicked(id) {
        this.props.history.push(`/admin/${id}`);
    }

    componentDidMount() {
        this.getAllStudycoursesById();
        this.getAllModulesById();
        this.getAllModulePartsById();
        this.getAllSemesterById();
        this.getAllPersonsById();
        this.getAllSposById();
        this.getAllUsersById();

    }

    render() {
        const { classes } = this.props;
        const { loadingProgress, error, studycourses, modules, moduleparts, semester, person, spo, user} = this.state;
        return (

            <Box sx={{ width: '100%', maxWidth: 650 }}>
     
                <Typography variant="h6" textAlign={'center'} gutterBottom component="div">
                    SPO
                </Typography>
                    
                <Stack spacing={2} direction="column">
                    {
                        studycourses.map((studycourse) => (
                        <Button
                            variant="contained"
                            key={studycourse.id}
                            onClick={this.buttonNavigateToCourseClicked.bind(this, studycourse.id)}
                            show ={this.props.show}>
                                {studycourse.title}
                        </Button>
                        ))
						
                    }
                </Stack>
				<Stack spacing={2} direction="column">
                    {
                        modules.map((module) => (
                        <Button
                            variant="contained"
                            key={module.id}
                            onClick={this.buttonNavigateToCourseClicked.bind(this, module.id)}
                            show ={this.props.show}>
                                {module.title}
                        </Button>
                        ))
						
                    }
                </Stack>
            </Box>
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
AdminSpoAnsicht.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** @ignore */
    location: PropTypes.object.isRequired,
   
}


export default withRouter(withStyles(styles)(AdminSpoAnsicht));