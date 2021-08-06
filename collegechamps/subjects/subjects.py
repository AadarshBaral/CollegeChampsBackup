from flask import render_template, request, Blueprint
from collegechamps.models import User, Post

subjects = Blueprint('subjects', __name__)

maths_sub ={
    "header":'Mathematics',
    "sub_header": 'The Heart of All Sciences',
    "topics" : [{'Sets And Functions':'sets_and_functions'},{'Algebra':'algebra'},{'Trigonometry':'trigonometry'},{'Coordinate Geometry':'coordinate_geometry'},{'Claculus':'calculus'},{'Vectors':'vectors'}
    ]
}
physics_sub ={
    "header":'Physcis',
    "sub_header": 'Defines the universe',
        "topics" : [{'Mechanics':'mechanics'}, {'Optics':'optics'},{'Heat':'heat'},{'Atomic Plysics & Electrostats':'electrostatics',},{'Sound':'sound'}]
}
chemistry_sub ={
    "header":'Chemistry',
    "sub_header": 'Defines the universe',
    # {title : route}
    "topics" : [{'Language of Chemistry':'physical_chemistry'}, {'Electronic theory to valency':'electronic_theory_to_valency'},
    # have to replace the _ with space
    {'Oxidation and Reduction':'oxidation_and_reduction'},{'Periodic Table':'periodic_table',},{'Mole Concept':'mole_concept'},{'Non-Metals':'non_metals'},{'Metals':'metals'},{'Organic Chemistry':'organic_chemistry'}]
}
biology_sub ={
    "header":'Biology',
    "sub_header": 'Defines the universe',
    "topics" : ['Mechanics', 'Optics','Thermodynamics','Gas Laws','Electrostats']
}


@subjects.route('/maths')
def maths():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html', heading  = maths_sub['header'],sub_header = maths_sub['sub_header'], topics = maths_sub['topics'], background = 'sc-4', button = 'sc4-btn', cardBackground = 'backMathCard',side_posts = side_posts)

@subjects.route('/physics')
def physics():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html', heading  = physics_sub['header'],sub_header = physics_sub['sub_header'],
     topics = physics_sub['topics'], background = 'sc-1',
     button = 'sc1-btn' , cardBackground = 'backPhyCard', side_posts = side_posts)


@subjects.route('/biology')
def biology():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html', heading  = biology_sub['header'],
    sub_header = biology_sub['sub_header'], topics = biology_sub['topics'], 
    background = 'sc-3', button = 'sc3-btn', cardBackground = 'backBioCard',id = len(biology_sub), side_posts= side_posts)


@subjects.route('/chemistry')
def chemistry():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html',side_posts=side_posts, heading  = chemistry_sub['header'],
    sub_header = chemistry_sub['sub_header'], topics = chemistry_sub['topics'],
     background = 'sc-2', button = 'sc2-btn' , cardBackground = 'backChemCard')


@subjects.route('/set_prep_page')
def set_prep_page():
    sets = Post.query.filter_by(slug='set_page')

    return render_template('subject_sets.html', sets=sets)


@subjects.route('/individual_set/<int:set_id>')
def individual_set(set_id):
    time_limit = 28
    individual_page = Post.query.get_or_404(set_id)
    return render_template('forms_page.html', individual_page=individual_page,time_limit = time_limit)

# Physics
# Physics
# Physics

@subjects.route('/ioe-mechanics-entrance-questions')
def mechanics():
    #for these routes  i will need the to_redirect slug and it will redirect to set page where students will be able to choose different test sets.
    #there will be no individual id link in this route.
    sets = Post.query.filter_by(slug='set_page', subject_title = 'mechanics')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Mechanics Pracice Questions' ,header='Mechanics Sets')


@subjects.route('/ioe-physics/ioe-optics-questions')
def optics():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'optics')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Optics Pracice Questions' ,header='Optics Sets')

@subjects.route('/ioe-physics/ioe-heat-and-thermodynamics')
def heat():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'heat')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Heat Pracice Questions' ,header='Heat Sets')

@subjects.route('/ioe-physics/ioe-sound')
def sound():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'sound')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Sound Pracice Questions' ,header='Sound Sets')


@subjects.route('/ioe-physics/ioe-atomic-physics-electrostatics')
def electrostatics():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'elect_atom')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Electrostacics And Atom Pracice Questions' ,header='Electricity and Atom Sets')


# Chemistry
# Chemistry
# Chemistry
@subjects.route('/ioe-chemistry/ioe-chemistry-language-of-chemistry-&-physical-chemistry')
def physical_chemistry():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'phy-chem')
    return render_template('subject_sets.html', sets=sets,title = ' IOE Language of Chemistry & Physical Chemistry' ,header='Language of Chemistry & Physical Chemistry')


@subjects.route('/ioe-chemistry/ioe-chemistry-electronics-theory-to-valency')
def electronic_theory_to_valency():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'valency')
    return render_template('subject_sets.html', sets=sets,title = ' IOE Electronics Theory to Valency' ,header='Electronics Theory To Valency')

@subjects.route('/ioe-chemistry/ioe-chemistry-oxidation-and-reduction')
def oxidation_and_reduction():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'oxidation')
    return render_template('subject_sets.html', sets=sets,title = ' IOE Oxidation And Reduction' ,header='Oxidation and Reduction')

@subjects.route('/ioe-chemistry/ioe-chemistry-periodic-table')
def periodic_table():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'periodic_table')
    return render_template('subject_sets.html', sets=sets,title = ' IOE Periodic Table' ,header='Periodic Table')

@subjects.route('/ioe-chemistry/ioe-chemistry-molecular-weight-and-mole')
def mole_concept():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'mole')
    return render_template('subject_sets.html', sets=sets,title = ' IOE Molecular Theory And Mole' ,header='Mole Concept and Molecular Theory')

@subjects.route('/ioe-chemistry/ioe-chemistry-metals')
def metals():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'metals')
    return render_template('subject_sets.html', sets=sets,title = ' IOE Metals' ,header='Metals')

@subjects.route('/ioe-chemistry/ioe-chemistry-non-metals')
def non_metals():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'n-metals')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Non-Metals' ,header='Non-Metals')

@subjects.route('/ioe-chemistry/ioe-chemistry-organic-chemistry')
def organic_chemistry():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'organic')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Organic Chemitry' ,header='Organic Chemistry')

#mathematics
#mathematics
#mathematics
@subjects.route('/ioe-mathematics/ioe-maths-set-and-function')
def sets_and_functions():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'set_function')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Sets And Function' ,header='Sets & Functions')

@subjects.route('/ioe-mathematics/ioe-algebra')
def algebra():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'algebra')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Sets And Function' ,header='Algebra')

@subjects.route('/ioe-mathematics/ioe-trigonometry')
def trigonometry():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'trigonometry')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Trignonmetry' ,header='Trigonometry')

@subjects.route('/ioe-mathematics/ioe-co-ordinate_geometry')
def coordinate_geometry():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'coord_geometry')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Co-ordinate Geometry' ,header='Co-ordinate Geometry')

@subjects.route('/ioe-mathematics/ioe-calculus-derivatives-and-antiderivatives')
def calculus():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'calculus')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Calculus' ,header='Calculus')

# @subjects.route('/ioe-mathematics/ioe-calculus-derivatives-and-antiderivatives')
# def calculus():
#     sets = Post.query.filter_by(slug='set_page', subject_title = 'calculus')
#     return render_template('subject_sets.html', sets=sets,title = 'IOE Calculus' ,header='Calculus')

@subjects.route('/ioe-mathematics/ioe-vectors')
def vectors():
    sets = Post.query.filter_by(slug='set_page', subject_title = 'vectors')
    return render_template('subject_sets.html', sets=sets,title = 'IOE Vectors' ,header='Vectors')


















