PGDMP                         z           movies    14.5    14.5     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    24593    movies    DATABASE     c   CREATE DATABASE movies WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE movies;
                postgres    false            ?            1259    24594    films    TABLE     u   CREATE TABLE public.films (
    actors text NOT NULL,
    film text NOT NULL,
    director character varying(100)
);
    DROP TABLE public.films;
       public         heap    postgres    false            ?            1259    24609    students    TABLE     V   CREATE TABLE public.students (
    id integer NOT NULL,
    fullname text NOT NULL
);
    DROP TABLE public.students;
       public         heap    postgres    false            ?            1259    24614    students_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.students_id_seq;
       public          postgres    false    212            ?           0    0    students_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;
          public          postgres    false    213            b           2604    24630    students id    DEFAULT     j   ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);
 :   ALTER TABLE public.students ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    212            ?          0    24594    films 
   TABLE DATA           7   COPY public.films (actors, film, director) FROM stdin;
    public          postgres    false    211   ?
       ?          0    24609    students 
   TABLE DATA           0   COPY public.students (id, fullname) FROM stdin;
    public          postgres    false    212   ?       ?           0    0    students_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.students_id_seq', 1, false);
          public          postgres    false    213            ?   ?   x??An1??+?y??ђE( q?eX&x??8?$?ù??^?K?֩?????? ??&?@J??0҅ޝl????0z?dî?X)?? ??6?*{	_??@&??H????׽X{+?n??/X??S?5?&vl???1???j\k?g??6?ү?S???-5?4M?]?~?1?lJ?      ?      x?????? ? ?     