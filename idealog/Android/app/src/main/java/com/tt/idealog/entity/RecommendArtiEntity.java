package com.tt.idealog.entity;

public class RecommendArtiEntity {
    String title;
    String content;
    String writer;
    String numOfLikes;
    String numOfComment;

    public RecommendArtiEntity(String title, String content, String writer, String numOfLikes, String numOfComment) {
        this.title = title;
        this.content = content;
        this.writer = writer;
        this.numOfLikes = numOfLikes;
        this.numOfComment = numOfComment;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void setWriter(String writer) {
        this.writer = writer;
    }

    public void setNumOfLikes(String numOfLikes) {
        this.numOfLikes = numOfLikes;
    }

    public void setNumOfComment(String numOfComment) {
        this.numOfComment = numOfComment;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getWriter() {
        return writer;
    }

    public String getNumOfLikes() {
        return numOfLikes;
    }

    public String getNumOfComment() {
        return numOfComment;
    }
}
