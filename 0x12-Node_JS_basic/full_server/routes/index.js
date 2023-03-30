import AppController from '../controllers/AppController'
import StudentsController from '../controllers/StudentsController'
import express from 'express'

const router = express.Router();

router.get('/', AppController.getHomepage);

router.get('/students', StudentsController.getAllStudents);

router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
