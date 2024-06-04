import pytest
from classes.many_to_many import Author, Magazine, Article

class TestAuthor:
    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        
        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)
        
    
    def test_articles(self):
        """author has a list of articles"""
        author = Author("Carry Bradshaw")
        assert isinstance(author.articles(), list)

    def test_magazines(self):
        """author has a list of magazines"""
        author = Author("Carry Bradshaw")
        assert isinstance(author.magazines(), list)

    def test_add_article(self):
        """author can add an article to a magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "How to wear a tutu with style")
        assert isinstance(article, Article)
        assert article in author.articles()
        assert article in magazine.articles()

    def test_topic_areas(self):
        """author has a list of topic areas based on articles written"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "Carrara Marble is so 2020")
        assert isinstance(author.topic_areas(), list)
        assert "Fashion" in author.topic_areas()
        assert "Architecture" in author.topic_areas()

class TestMagazine:
    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)
        
        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"
        
       
    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16
       

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)
        
        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"
        
        assert isinstance(magazine_1.category, str)
     

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")
        
        assert magazine_1.category != ""
        

    def test_contributing_authors(self):
        """returns author list who have written more than 2 articles for the magazine"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        Article(author_2, magazine_2, "2023 Eccentric Design Trends")
        
        assert author_1 in magazine_1.contributing_authors()
        assert author_2 not in magazine_1.contributing_authors()
        assert all(isinstance(author, Author) for author in magazine_1.contributing_authors())
        
        
        assert magazine_2.contributing_authors() == []

