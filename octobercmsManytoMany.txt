#First we want to go to the builder and create a new plugin- we will call it blogpost
#inside the backend builder plugin click on the database
#we will create three databases

ten31_blog_posts
    id - Integer - unsigned-autoincr

ten31_blog_tags
    id - integer - unsigned - autoincr
    title - String
    slug - string

#this will be our join table that connects the posts with the tags
ten31_blog_posts_tags 
    blog_post_id - integer - unsigned - pk
    tags_id - integer - unsigned - pk


#now go inside models/blogpost/fields.yaml and add the following to create the fields for our backend form

fields:
    tags:
        label: Tags
        type: partial
        path: field_tags
        nameFrom: title


#we also want to be able to create a form for the tags so go inside models/tags/fields.yaml and this will create the backend form
fields:
    title:
        label: 'ten31.blog::lang.tags.title'
        oc.commentPosition: ''
        span: auto
        type: text
    slug:
        label: 'ten31.blog::lang.tags.slug'
        oc.commentPosition: ''
        span: auto
        preset:
            field: title
            type: slug
        type: text


#next go inside BlogPost.php inside the models folder and connect the blogpost with tags by adding a many to many relationship
#models/BlogPost.php

  public $belongsToMany = [
        'tags' => [
            'Ten31\Blog\Models\Tags',
            'table' => 'ten31_blog_posts_tags',
        ],
    ];



#inside models/Tags.php

 public $hasOne = [];
    public $hasMany = [];
    public $belongsTo = [];
    public $belongsToMany = [];
    public $morphTo = [];
    public $morphOne = [];
    public $morphMany = [];
    public $attachOne = [];
    public $attachMany = [];


#create a new file in controllers named config_relation and inside config relation we create how we will interact with our many to many relationship

tags:
    label: Tags
    view:
        list: $/ten31/blog/models/tags/columns.yaml
        toolbarButtons: create|add|remove
    manage:
        form: $/ten31/blog/models/tags/fields.yaml

#we now need to create a partial that will render our tags in the backend form, this will be connected to our blogpost
#in the controller file blogpost create a new file called _field_tags.htm

<?= $this->relationRender('tags') ?>

#this renders the partial to display in the backend form for our blogpost





